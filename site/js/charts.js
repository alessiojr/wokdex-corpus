/**
 * WOKDEX Corpus — Charts Module
 * Canvas-based charts for the dashboard (no external dependencies).
 */

const Charts = (() => {
  const COLORS = {
    cyan: '#06b6d4',
    blue: '#3b82f6',
    green: '#22c55e',
    orange: '#f97316',
    red: '#ef4444',
    purple: '#a855f7',
    yellow: '#eab308',
    pink: '#ec4899',
    teal: '#14b8a6',
    indigo: '#6366f1',
  };

  const COLOR_ARRAY = Object.values(COLORS);

  /**
   * Draw a horizontal bar chart.
   */
  function drawBarChart(canvasId, data, options = {}) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const dpr = window.devicePixelRatio || 1;

    const rect = canvas.parentElement.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = (options.height || 280) * dpr;
    canvas.style.width = rect.width + 'px';
    canvas.style.height = (options.height || 280) + 'px';
    ctx.scale(dpr, dpr);

    const w = rect.width;
    const h = options.height || 280;
    const padding = { top: 20, right: 20, bottom: 40, left: 120 };

    const labels = Object.keys(data);
    const values = Object.values(data);
    const maxVal = Math.max(...values, 1);

    const barH = Math.min(32, (h - padding.top - padding.bottom) / labels.length - 8);
    const gap = 8;

    ctx.clearRect(0, 0, w, h);

    labels.forEach((label, i) => {
      const y = padding.top + i * (barH + gap);
      const barW = ((w - padding.left - padding.right) * values[i]) / maxVal;

      // Bar
      const gradient = ctx.createLinearGradient(padding.left, 0, padding.left + barW, 0);
      const color = options.colors?.[label] || COLOR_ARRAY[i % COLOR_ARRAY.length];
      gradient.addColorStop(0, color);
      gradient.addColorStop(1, color + '88');

      ctx.fillStyle = gradient;
      ctx.beginPath();
      ctx.roundRect(padding.left, y, barW, barH, 4);
      ctx.fill();

      // Label
      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px Inter, sans-serif';
      ctx.textAlign = 'right';
      ctx.textBaseline = 'middle';
      ctx.fillText(label, padding.left - 10, y + barH / 2);

      // Value
      ctx.fillStyle = '#f1f5f9';
      ctx.font = '600 12px Inter, sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText(values[i].toString(), padding.left + barW + 8, y + barH / 2);
    });
  }

  /**
   * Draw a donut/pie chart.
   */
  function drawDonutChart(canvasId, data, options = {}) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const dpr = window.devicePixelRatio || 1;

    const size = options.size || 240;
    canvas.width = size * dpr;
    canvas.height = size * dpr;
    canvas.style.width = size + 'px';
    canvas.style.height = size + 'px';
    ctx.scale(dpr, dpr);

    const cx = size / 2;
    const cy = size / 2;
    const radius = size / 2 - 20;
    const innerRadius = radius * 0.55;

    const labels = Object.keys(data);
    const values = Object.values(data);
    const total = values.reduce((a, b) => a + b, 0);

    const colorMap = {
      'TDD': COLORS.green,
      'TDD_FALSE_GREEN': COLORS.orange,
      'PERFORMANCE': COLORS.red,
      'SAMPLE': COLORS.purple,
      'INPUT': COLORS.blue,
      'E': COLORS.green,
      'D': COLORS.blue,
      'C': COLORS.yellow,
      'B': COLORS.orange,
      'A': COLORS.red,
    };

    ctx.clearRect(0, 0, size, size);

    let startAngle = -Math.PI / 2;

    labels.forEach((label, i) => {
      const sliceAngle = (values[i] / total) * Math.PI * 2;
      const color = colorMap[label] || COLOR_ARRAY[i % COLOR_ARRAY.length];

      ctx.beginPath();
      ctx.arc(cx, cy, radius, startAngle, startAngle + sliceAngle);
      ctx.arc(cx, cy, innerRadius, startAngle + sliceAngle, startAngle, true);
      ctx.closePath();
      ctx.fillStyle = color;
      ctx.fill();

      // Hover gap effect
      ctx.strokeStyle = '#0a0e1a';
      ctx.lineWidth = 2;
      ctx.stroke();

      startAngle += sliceAngle;
    });

    // Center text
    ctx.fillStyle = '#f1f5f9';
    ctx.font = '700 24px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(total.toString(), cx, cy - 8);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('total', cx, cy + 14);
  }

  /**
   * Draw a legend for any chart.
   */
  function drawLegend(containerId, data, options = {}) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const colorMap = {
      'TDD': COLORS.green,
      'TDD_FALSE_GREEN': COLORS.orange,
      'PERFORMANCE': COLORS.red,
      'SAMPLE': COLORS.purple,
      'INPUT': COLORS.blue,
      'E': COLORS.green,
      'D': COLORS.blue,
      'C': COLORS.yellow,
      'B': COLORS.orange,
      'A': COLORS.red,
    };

    const labels = Object.keys(data);
    const values = Object.values(data);
    const total = values.reduce((a, b) => a + b, 0);

    container.innerHTML = labels
      .map((label, i) => {
        const color = colorMap[label] || COLOR_ARRAY[i % COLOR_ARRAY.length];
        const pct = total > 0 ? Math.round((values[i] / total) * 100) : 0;
        const displayLabel = options.labels?.[label] || label;
        return `
          <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
            <span style="width:12px;height:12px;border-radius:3px;background:${color};flex-shrink:0;"></span>
            <span style="font-size:0.8rem;color:#94a3b8;">${displayLabel}</span>
            <span style="font-size:0.8rem;font-weight:600;color:#f1f5f9;margin-left:auto;">${values[i]} (${pct}%)</span>
          </div>`;
      })
      .join('');
  }

  return { drawBarChart, drawDonutChart, drawLegend, COLORS };
})();
