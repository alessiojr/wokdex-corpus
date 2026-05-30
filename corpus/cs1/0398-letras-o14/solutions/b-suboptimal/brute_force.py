import sys

def main():
    try:
        char = input().strip()
        text = input().strip()
    except EOFError:
        return
        
    # Inefficient parsing: Character by character string concatenation
    words = []
    current_word = ""
    for c in text:
        if c == ' ':
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += c
    if current_word:
        words.append(current_word)
        
    if not words:
        print("0.0")
        return
        
    # Inefficient checking: manual character matching loop instead of built-in operator
    count = 0
    for w in words:
        found = False
        for c in w:
            if c == char:
                found = True
                break
        if found:
            count += 1
            
    ans = (count / len(words)) * 100.0
    print(f"{ans:.1f}")

if __name__ == '__main__':
    main()
