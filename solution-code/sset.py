if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_sset.txt"
    file = open(file_path, "r").readline()
    n = int(file)
    print(n)
    print((2**n)%1000000)