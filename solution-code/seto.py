import os

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_seto.txt"
    solution_path = "../solution-outputs/rosalind_seto.txt"
    file = open(file_path, 'r')
    lines = file.readlines()
    n = lines[0]
    A = lines[1]
    B = lines[2]

    B = str(B).replace('{', '').replace('}', '')
    ListB = []
    for item in B.split(','):
        ListB.append(int(item))
    SetB = set(ListB)
    A = str(A).replace('{', '').replace('}', '')
    ListA = []
    for item in A.split(','):
        ListA.append(int(item))
    SetA = set(ListA)
    n = int(n)
    ListN = []
    for i in range(1, n + 1):
        ListN.append(i)
    SetN = set(ListN)

    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(str(SetA.union(SetB)))
    file.write('\n')
    file.write(str(SetA.intersection(SetB)))
    file.write('\n')
    file.write(str(SetA.difference(SetB)))
    file.write('\n')
    file.write(str(SetB.difference(SetA)))
    file.write('\n')
    file.write(str(SetN.difference(SetA)))
    file.write('\n')
    file.write(str(SetN.difference(SetB)))
    file.close()

