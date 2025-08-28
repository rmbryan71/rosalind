import math

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)

def comb(n, k):
    return fact(n) // (fact(k)*fact(n - k))

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_aspc.txt"
    file = open(file_path, "r").readline().split(' ')
    n = int(file[0])
    m = int(file[1])
    print(n, m)
    result1 = 0
    # result2 = 0
    for i in range(m, n+1):
        result1 += math.comb(n, i)
        result1 %= 1000000
    # for j in range(m, n+1):
    #     result2 += comb(n, j)
    #     result2 %= 1000000
    print("Math library result = ", result1)
    # print("My equation result = ", result2)
