from itertools import combinations

def flip(x, i, j):
    """Flip a section of a sequence"""
    rev = list.copy(x)
    rev[i:j] = rev[i:j][::-1]
    return rev

def breaks(s, t):
    """Identify breaks between a sequence and target"""
    return [
        i + 1 for i in range(len(s) - 1) if abs(t.index(s[i]) - t.index(s[i + 1])) != 1
    ]

def min_breaks(seqs, t):
    rev = []
    for s in seqs:
        for i, j in combinations(breaks(s["s"], t), 2):
            rev.append({"s": flip(s["s"], i, j), "p": s["p"] + [[i, j - 1]]})
    min_b = len(t)
    mr = []
    for r in rev:
        n = len(breaks(r["s"], t))
        if n < min_b:
            min_b = n
            mr = [r]
        elif n == min_b:
            mr.append(r)
    return mr

def sort(s, t):
    """Sorting by Reversals"""
    s = ["-"] + s + ["+"]
    t = ["-"] + t + ["+"]
    nr = 0
    c = [{"s": s, "p": []}]
    seqs = [s]
    while t not in seqs:
        c = min_breaks(c, t)
        nr += 1
        seqs = [x["s"] for x in c]
    return nr, c

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_sort_sample.txt"
    with open(file_path) as file:
        d = [line.strip() for line in file.readlines()]
    s, t = d[0], d[1]
    s = list(map(int, s.split()))
    t = list(map(int, t.split()))
    nr, c = sort(s, t)
    print(nr)
    for r in c[0]["p"]:
        print(*r)
