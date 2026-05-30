import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    while idx < len(input_data):
        r = int(input_data[idx])
        idx += 1
        if r == 0:
            break
            
        m = [int(x) for x in input_data[idx:idx+r]]
        idx += r
        l = [int(x) for x in input_data[idx:idx+r]]
        idx += r
        
        score_m = 0
        score_l = 0
        bonus_given = False
        
        for i in range(r):
            score_m += m[i]
            score_l += l[i]
            
            if not bonus_given and i >= 2:
                m_consec = (m[i] == m[i-1] == m[i-2])
                l_consec = (l[i] == l[i-1] == l[i-2])
                
                if m_consec and l_consec:
                    bonus_given = True
                elif m_consec:
                    score_m += 30
                    bonus_given = True
                elif l_consec:
                    score_l += 30
                    bonus_given = True
                    
        if score_m > score_l:
            print("M")
        elif score_l > score_m:
            print("L")
        else:
            print("T")

if __name__ == '__main__':
    main()
