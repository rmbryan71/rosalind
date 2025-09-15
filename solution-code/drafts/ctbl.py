from Bio import Phylo
from io import StringIO
import re

def nodes(graph):
    s = list(graph.keys())
    e = [y["n"] for v in graph.values() for y in v]
    return set(s) | set(e)

def descendants(T):
    def recurse(node):
        if node not in T:
            d[node] = []
            return []
        if node not in d:
            children = [x["n"] for x in T[node]]
            d[node] = children + [y for x in T[node] for y in recurse(x["n"])]
            return d[node]

    d = {}
    recurse("0")
    return d

def ctbl(tree):
    desc = descendants(tree)
    allnodes = sorted(x for x in nodes(tree) if not re.match(r"^\d+$", x))
    for subnodes in desc.values():
        if not len(subnodes) or all([x in subnodes for x in allnodes]):
            continue
        yield "".join(["1" if n in subnodes else "0" for n in allnodes])

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_ctbl_sample.txt"
    with open(file_path, "r") as f:
        handle = StringIO(f.readline().rstrip())
        tree = Phylo.read(handle, 'newick')
        for code in ctbl(tree):
            print(code)