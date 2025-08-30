from itertools import groupby

def trie(seqs):
    graph = {}
    if len(seqs):
        for base, nseqs in groupby(sorted(seqs), key=lambda s: s[0]):
            graph[base] = trie([seq[1:] for seq in nseqs if len(seq) > 1])
    return graph

def as_adjacency(graph, nodes=[]):
    node = len(nodes) + 1
    for edge in sorted(graph):
        i = len(nodes) + 1
        nodes.append((node, i + 1, edge))
        nodes + as_adjacency(graph[edge], nodes)
    return nodes

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_trie_sample.txt"
    file = open(file_path, "r").readlines()
    strings = []
    for line in file:
        strings.append(line.strip())
    print(strings)
    # print(trie(strings))
    for edge in as_adjacency(trie(strings)):
        print(*edge)