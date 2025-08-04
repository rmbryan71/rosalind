import itertools

def lexv(A, n):
    result = []
    for i in range(1, n+1):
        for x in itertools.combinations_with_replacement(A, i):
            result.append(str(''.join(x)))
    return result

def mysort(n):
    return A.find(n)

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_lexv.txt"
    solution_path = "../solution-outputs/rosalind_lexv.txt"
    file = open(file_path, "r").readlines()
    A = str(file[0]).strip().replace(' ','')
    n = int(file[1])
    answer = sorted((lexv(A, n)), key=mysort)
    print(answer)