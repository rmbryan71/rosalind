import os

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_subs.txt"
    solution_path = "../solution-outputs/rosalind_subs.txt"
    file = open(file_path, "r").readlines()
    s = file[0]
    t = file[1]
    ### Solving code goes here
    def subs(s, t):
        solution = ''
        for i in range(0, len(s) - 1):
            if (s[i:i+len(t)]) == t:
                solution += str(i + 1)
                solution += ' '
        return solution
    solution = subs(s, t)
    ### End of solving code
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(solution)
    file.close()
    print(solution)