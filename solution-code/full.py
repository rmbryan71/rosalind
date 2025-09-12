def protein_mass():
    with open ('proteinmass.txt') as mass:
        d = {}
        for i in mass:
            t = i.split()
            d[t[0]] = float(t[1])
    return d

def infer_peptide(current, remain, d):
    for i in remain:
        for j in d:
            if abs(d[j] - (i-current)) < 0.001:
                return j
    return -1

def all_seq(ions, d):
    n = (len(ions)-2)/2
    res = ''
    current = ions[0]
    remain = ions[1:]

    while len(res) < n:
        temp = infer_peptide(current, remain, d)
        if temp == -1:
            return res
        else:
            res += temp
            current += d[temp]
            remain = filter(lambda x: x - current > 0, remain)
    return res

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_full.txt"
    file = open(file_path, "r").readlines()
    L = []
    for line in file:
        L.append(float(line.strip()))
    parent_mass = L.pop(0)
    ions = sorted(L)
    d = protein_mass()
    print(all_seq(ions, d))

