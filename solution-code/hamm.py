import os

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_hamm.txt"
    solution_path = "../solution-outputs/rosalind_hamm.txt"
    file = open(file_path, "r").readlines()
    a = file[0]
    b = file[1]
    ### Solving code goes here
    def hamm(a, b):
        solution = 0
        length = len(a)
        for i in range(0, length - 1):
            if a[i] != b[i]:
                solution += 1
        return str(solution)
    solution = hamm(a, b)
    ### End of solving code
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(solution)
    file.close()
    print(solution)