import os

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_perm.txt"
    solution_path = "../../solution-outputs/rosalind_perm.txt"
    n = int(open(file_path, "r").readline())



    if os.path.exists(solution_path):
        os.remove(solution_path)
    file = open(solution_path, "x")
    file.write(str(factorial(n)))
    file.close()
