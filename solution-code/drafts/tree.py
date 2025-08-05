if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_tree.txt"
    solution_path = "../solution-outputs/rosalind_tree.txt"
    file = open(file_path, "r").readlines()
    n = file[0]
    print(n)
    edges = []
    for line in file[1:]:
        line = line.strip().split(' ')
        edges.append(line)
    print(edges)
    strnodes = []
    for edge in edges:
        for node in edge:
            if node not in strnodes:
                strnodes.append(node)
    intnodes = []
    for node in strnodes:
        intnodes.append(int(node))
    intnodes.sort()
    print(intnodes)