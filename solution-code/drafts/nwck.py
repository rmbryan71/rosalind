from Bio import Phylo
from io import StringIO

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_nwck_sample.txt"
    file = open(file_path, "r").readlines()
    trees = []
    for index in range(len(file)):
        if file[index].find(';') > 0:
            trees.append((file[index].strip(), file[index + 1].strip().split(' ')))
    # print(trees)
    for tree in trees:
        # print(tree)
        handle = StringIO(tree[0])
        thistree = Phylo.read(handle, "newick")
        # print(tree[1][0])
        # print(tree[1][1])
        clades = thistree.find_clades()
        for clade in clades:
            clade.branch_length = 1
        distance = thistree.distance(tree[1][0], tree[1][1])
        print(distance, end=' ')

