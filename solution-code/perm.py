import os

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def permutations(input):
    if len(input) == 0:
        return []
    if len(input) == 1:
        return [input]
    set = []
    for j in range(len(input)):
        element = input[j]
        remainder = input[:j] + input[j+1:]
        for p in permutations(remainder):
            set.append([element] + p)
    return set



if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_perm.txt"
    solution_path = "../solution-outputs/rosalind_perm.txt"
    n = int(open(file_path, "r").readline())
    set = []
    for i in range(1, n + 1):
        set.append(i)
    perms = permutations(set)
    if os.path.exists(solution_path):
        os.remove(solution_path)
    file = open(solution_path, "x")
    file.write(str(factorial(n)))
    file.write('\n')
    for perm in perms:
        file.write(str(perm).replace('[','').replace(']', '').replace(',',''))
        file.write('\n')
    file.close()
