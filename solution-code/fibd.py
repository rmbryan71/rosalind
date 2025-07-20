import os

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_fibd.txt"
    solution_path = "../solution-outputs/rosalind_fibd.txt"
    file = open(file_path, "r").readline().split(' ')
    n = int(file[0])
    m = int(file[1])
    ### Solving code goes here
    def fib(n, m):
        history = [0, 1, 1]
        generations = 2
        for i in range(2, n):
            if i < m:
                history.append(history[-1] + history[-2])
            if i == m:
                history.append(history[-1] + history[-2] - 1)
            if i > m:
                history.append((history[-1] + history[-2]) - history[-m-1])
        print(history)
        return history[-1]
    solution = str(fib(n, m))
    ### End of solving code
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(solution)
    file.close()
    print(solution)