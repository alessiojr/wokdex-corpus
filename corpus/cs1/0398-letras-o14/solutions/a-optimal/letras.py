import sys

def main():
    try:
        char = input().strip()
        text = input().strip()
    except EOFError:
        return
        
    words = text.split()
    if not words:
        print("0.0")
        return
        
    count = sum(1 for w in words if char in w)
    
    ans = (count / len(words)) * 100.0
    print(f"{ans:.1f}")

if __name__ == '__main__':
    main()
