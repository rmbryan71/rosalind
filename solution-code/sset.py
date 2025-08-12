if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_sset.txt"
    solution_path = "../solution-outputs/rosalind_sset.txt"
    file = open(file_path, "r").readline()
    n = int(file)
    print((2**n)%1000000)