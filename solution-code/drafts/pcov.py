def dbru(seqs):
    return [(x[:-1], x[1:]) for x in seqs]


def find_cycle(graph):
    key = sorted(list(graph.keys()))[0]
    visited = set()
    cycle = []
    while key not in visited:
        cycle += [key]
        visited.add(key)
        key = graph[key]
    return cycle


def join_cycle(chain):
    return "".join(x[0] for x in chain)


def pcov(seqs):
    """Genome Assembly with Perfect Coverage"""
    x = find_cycle(dict(dbru(seqs)))
    return join_cycle(x)

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_pcov.txt"
    reads = []
    with open(file_path) as file:
        for line in file:
            reads.append(str(line.strip()))
    print(pcov(reads))

