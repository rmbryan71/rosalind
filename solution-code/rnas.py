from functools import cache

def isComplement(a, b):
    if a == 'A' and b == 'U':
        return True
    if a == 'U' and b == 'A':
        return True
    if a == 'C' and b == 'G':
        return True
    if a == 'G' and b == 'C':
        return True
    if a == 'U' and b == 'G':
        return True
    if a == 'G' and b == 'U':
        return True
    else:
        return False

@cache
def rnas(rna):
    if len(rna) == 1:
        return 1
    if len(rna) == 0:
        return 1
    else:
        return (
            rnas(rna[1:])
            + sum(
                rnas(rna[1:m]) * rnas(rna[m + 1 :])
                for m in range(4, len(rna))
                if isComplement(rna[0], rna[m])
            )
        )

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_rnas.txt"
    with open(file_path) as file:
        s = str(file.readline())
    print(s)
    print(len(s))
    print(rnas(s))