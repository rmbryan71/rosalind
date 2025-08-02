if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_lexf.txt"
    solution_path = "../solution-outputs/rosalind_lexf.txt"
    file = open(file_path, "r").readlines()
    A = str(file[0]).strip().replace(' ','')
    n = int(file[1])
