import os

def lexv(A, n):
    A = A[::-1]
    stack = [(letter,) for letter in A]

    while stack:
        string = stack.pop()
        yield ''.join(string)
        if len(string) != n:
            for letter in A:
                stack.append((*string, letter))

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_lexv.txt"
    solution_path = "../../solution-outputs/rosalind_lexv.txt"
    file = open(file_path, "r").readlines()
    A = str(file[0]).strip().replace(' ','')
    n = int(file[1])
    solution = list(lexv(A, n))
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    for item in solution:
        file.write(item + '\n')
    file.close()