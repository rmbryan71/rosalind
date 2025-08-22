import os

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_seto_sample.txt"
    B, A, n = set(line.strip() for line in open(file_path))
    B = str(B).replace('{', '').replace('}', '')
    ListB = []
    for item in B.split(','):
        ListB.append(int(item))
    print(ListB)
    A = str(A).replace('{', '').replace('}', '')
    ListA = []
    for item in A.split(','):
        ListA.append(int(item))
    print(ListA)
    n = int(n)
    print(n)
