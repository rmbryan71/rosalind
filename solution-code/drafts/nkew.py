from Bio import Phylo
from io import StringIO

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_nkew_sample.txt"
    with open(file_path, "r") as f:
        flines = f.readlines()
        for i in range(0, len(flines), 3):
            handle = StringIO(flines[i].rstrip())
            tree = Phylo.read(handle, 'newick')
            x, y = flines[i+1].rstrip().split()
            print(int(tree.distance(x,y)), end=' ')


