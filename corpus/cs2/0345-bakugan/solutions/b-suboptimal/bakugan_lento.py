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
        
        # Sub-optimal logic: recalculate sequence dynamically by scanning all previous elements and creating overhead
        score_m = sum(m)
        score_l = sum(l)
        
        bonus_given = False
        
        for i in range(r):
            # Artificially increasing complexity by checking arrays up to i in a loop
            # and recreating lists O(N^2) overall
            history_m = m[:i+1]
            history_l = l[:i+1]
            
            if not bonus_given and len(history_m) >= 3:
                m_consec = False
                l_consec = False
                
                for j in range(2, len(history_m)):
                    if history_m[j] == history_m[j-1] == history_m[j-2] and j == i:
                        m_consec = True
                
                for j in range(2, len(history_l)):
                    if history_l[j] == history_l[j-1] == history_l[j-2] and j == i:
                        l_consec = True
                        
                if m_consec and l_consec:
                    bonus_given = true
                elif m_consec:
                    score_m += 30
                    bonus_given = true
                elif l_consec:
                    score_l += 30
                    bonus_given = true
                    
        if score_m > score_l:
            print("M")
        elif score_l > score_m:
            print("L")
        else:
            print("T")

if __name__ == '__main__':
    main()
