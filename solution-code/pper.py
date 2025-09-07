def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)

def comb(n, k):
    return fact(n) // (fact(n - k))

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_pper.txt"
    file = open(file_path, "r").read().split(' ')
    n, k = int(file[0]), int(file[1])
    print(comb(n, k) % 1000000)