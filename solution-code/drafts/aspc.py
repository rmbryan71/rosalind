import math

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)

def comb(n, k):
    return fact(n) // fact(k)*fact(n - k)

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_aspc.txt"
    file = open(file_path, "r").readline().split(' ')
    n = int(file[0])
    m = int(file[1])
    print(n, m)
    result = 0
    for i in range(m, n+1):
        result += math.comb(n, i)
        result %= 1000000
    print(result)
