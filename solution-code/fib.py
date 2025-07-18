import os

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_fib.txt"
    solution_path = "../solution-outputs/rosalind_fib.txt"
    file = open(file_path, "r").readline().split(' ')
    n = int(file[0])
    k = int(file[1])
    ### Solving code goes here
    def fib(n, k):
        prev1, prev2 = 1, 1
        for i in range(2, n):
            current = prev1 + k * prev2
            prev2 = prev1
            prev1 = current
        return current
    solution = str(fib(n, k))
    ### End of solving code
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(solution)
    file.close()
    print(solution)