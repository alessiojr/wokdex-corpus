import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().splitlines()
    line_idx = 0
    
    while line_idx < len(input_data):
        line = input_data[line_idx].strip()
        if not line:
            line_idx += 1
            continue
        
        n = int(line)
        if n == 0:
            break
        
        line_idx += 1
        solved_at = {}      # problem_id -> first_correct_time
        incorrect_counts = {} # problem_id -> count_of_incorrect_before_correct
        
        for _ in range(n):
            parts = input_data[line_idx].split()
            prob = parts[0]
            time = int(parts[1])
            result = parts[2]
            
            # Submissions after the first 'correct' are ignored
            if prob not in solved_at:
                if result == "correct":
                    solved_at[prob] = time
                else:
                    incorrect_counts[prob] = incorrect_counts.get(prob, 0) + 1
            
            line_idx += 1
        
        total_solved = 0
        total_penalty = 0
        
        for prob, time in solved_at.items():
            total_solved += 1
            # Penalty = time + 20 * (incorrect submissions before the first correct)
            total_penalty += time + (incorrect_counts.get(prob, 0) * 20)
            
        print(f"{total_solved} {total_penalty}")

if __name__ == "__main__":
    solve()
