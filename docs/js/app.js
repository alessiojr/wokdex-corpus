/**
 * WOKDEX Corpus — Core Application
 * Handles data loading, navigation, and shared utilities.
 */

const App = (() => {
  let corpusData = null;
  let statsData = null;
  const cache = {};

  // Data paths (relative to site root)
  const DATA_BASE = 'data';

  /**
   * Load JSON data with caching.
   */
  async function loadJSON(path) {
    if (cache[path]) return cache[path];
    try {
      const resp = await fetch(path);
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      const data = await resp.json();
      cache[path] = data;
      return data;
    } catch (err) {
      console.error(`Failed to load ${path}:`, err);
      return null;
    }
  }

  /**
   * Load the main corpus index.
   */
  async function loadCorpus() {
    if (corpusData) return corpusData;
    corpusData = await loadJSON(`${DATA_BASE}/corpus.json`);
    return corpusData;
  }

  /**
   * Load aggregated stats.
   */
  async function loadStats() {
    if (statsData) return statsData;
    statsData = await loadJSON(`${DATA_BASE}/stats.json`);
    return statsData;
  }

  /**
   * Load a single exercise detail.
   */
  async function loadExercise(id) {
    return await loadJSON(`${DATA_BASE}/exercises/${id}.json`);
  }

  /**
   * Get URL query parameter.
   */
  function getParam(name) {
    return new URLSearchParams(window.location.search).get(name);
  }

  /**
   * Create a badge element.
   */
  function createBadge(text, type) {
    const span = document.createElement('span');
    span.className = `badge ${type}`;
    span.textContent = text;
    return span;
  }

  /**
   * Create test type badge.
   */
  function testTypeBadge(testType) {
    const map = {
      'TDD': { class: 'badge-tdd', label: 'TDD' },
      'TDD_FALSE_GREEN': { class: 'badge-false-green', label: 'FALSE GREEN' },
      'PERFORMANCE': { class: 'badge-performance', label: 'PERFORMANCE' },
      'SAMPLE': { class: 'badge-sample', label: 'SAMPLE' },
      'INPUT': { class: 'badge-tdd', label: 'INPUT' },
    };
    const info = map[testType] || { class: 'badge-skill', label: testType };
    return createBadge(info.label, info.class);
  }

  /**
   * Create difficulty badge.
   */
  function difficultyBadge(level) {
    return createBadge(level, `badge badge-difficulty badge-diff-${level}`);
  }

  /**
   * Animate number count-up.
   */
  function animateCount(element, target, duration = 1200) {
    const start = 0;
    const startTime = performance.now();

    function update(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      const current = Math.round(start + (target - start) * eased);
      element.textContent = current.toLocaleString('pt-BR');
      if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
  }

  /**
   * Initialize theme toggle (light/dark mode).
   */
  function initTheme() {
    const root = document.documentElement;
    const savedTheme = localStorage.getItem('wokdex-theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    // Apply saved or system theme
    if (savedTheme) {
      root.setAttribute('data-theme', savedTheme);
    } else if (!systemPrefersDark) {
      // System is light; CSS default is already light, no action needed
      root.setAttribute('data-theme', 'light');
    }
    // If systemPrefersDark and no saved preference, CSS @media handles it automatically

    // Wire up toggle button
    const toggleBtn = document.getElementById('theme-toggle');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', () => {
        const isDark = root.getAttribute('data-theme') === 'dark' ||
          (!root.hasAttribute('data-theme') && window.matchMedia('(prefers-color-scheme: dark)').matches);

        if (isDark) {
          root.setAttribute('data-theme', 'light');
          localStorage.setItem('wokdex-theme', 'light');
        } else {
          root.setAttribute('data-theme', 'dark');
          localStorage.setItem('wokdex-theme', 'dark');
        }
      });
    }
  }

  /**
   * Set up navigation mobile toggle.
   */
  function initNav() {
    const hamburger = document.querySelector('.nav-hamburger');
    const links = document.querySelector('.nav-links');
    if (hamburger && links) {
      hamburger.addEventListener('click', () => {
        links.classList.toggle('open');
      });
    }

    // Set active link
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-links a').forEach(a => {
      const href = a.getAttribute('href');
      if (href === currentPage || (currentPage === '' && href === 'index.html')) {
        a.classList.add('active');
      }
    });
  }

  /**
   * Intersection Observer for scroll animations.
   */
  function initScrollAnimations() {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
    );

    document.querySelectorAll('[data-animate]').forEach(el => {
      observer.observe(el);
    });
  }

  /**
   * Format difficulty label.
   */
  function difficultyLabel(level) {
    const labels = {
      'E': 'Fundamentos',
      'D': 'Iniciante',
      'C': 'Intermediário',
      'B': 'Especialista',
      'A': 'Avançado',
    };
    return labels[level] || level;
  }

  /**
   * Initialize common functionality.
   */
  function init() {
    initTheme();
    initNav();
    initScrollAnimations();
  }

  // Auto-init when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  return {
    loadCorpus,
    loadStats,
    loadExercise,
    getParam,
    createBadge,
    testTypeBadge,
    difficultyBadge,
    animateCount,
    difficultyLabel,
    initScrollAnimations,
    initTheme,
  };
})();
