from itertools import combinations

def subsets(set, length):
    return (len(list(combinations(set, length))))

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_sset.txt"
    solution_path = "../solution-outputs/rosalind_sset.txt"
    file = open(file_path, "r").readline()
    n = int(file)
    print(n)
    myset = []
    result = 1
    for i in range(1, n+1):
        myset.append(i)
    for j in range(1, n+1):
        # print(subsets(myset, j))
        result += subsets(myset, j)
        result %= 1000000
        print(j/n)
    print(result)