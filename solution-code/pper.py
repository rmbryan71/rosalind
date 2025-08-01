import scipy


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_pper.txt"
    file = open(file_path, "r").read().split(' ')
    n = int(file[0])
    k = int(file[1])
    print(n, k)
    part_perm = 1
    for i in range(k):
        part_perm *= (n - 1)
        part_perm %= 1000000
    print(part_perm)
    print(scipy.special.perm(n, k, exact=True) % 1000000)