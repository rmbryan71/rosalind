def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_pper.txt"
    solution_path = "../solution-outputs/rosalind_pper.txt"
    file = open(file_path, "r").read().split(' ')
    n = int(file[0])
    k = int(file[1])
    # print(n, k)
    numerator = factorial(n)
    denominator = factorial(k)*factorial(n - k)
    print((numerator//denominator) % 1000000)