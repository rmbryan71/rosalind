from Bio import Phylo
from io import StringIO

def ctbl(node, taxa):
    for child in node.clades:
        if not child.is_terminal():
            arr = [0 for i in range(len(taxa))]
            for child_node in child.find_clades():
                if child_node.name:
                    arr[taxa.index(child_node.name)] = 1
            for elt in arr:
                print(elt, end='')
            print()
            ctbl(child, taxa)


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_ctbl_sample.txt"
    tree = Phylo.read(file_path, 'newick')
    nodes = []
    for node in tree.find_clades():
        if node.name:
            nodes.append(node.name)
    nodes.sort()
    ctbl(tree.root, nodes)
