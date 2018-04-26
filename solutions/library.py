def load_data(code):
    filename = ('datasets/rosalind_' + code + '.txt')
    with open(filename) as f:
        read_data = f.read()
    return read_data


def parse_fasta(s):
    results = {}
    strings = s.strip().split('>')

    for s in strings:
        if len(s) == 0:
            continue

        parts = s.split()
        label = parts[0]
        values = ''.join(parts[1:])

        results[label] = values
    return results


def gc_load(i):
    n = len(i)
    m = 0
    for c in i:
        if c == 'G' or c == 'C':
            m += 1
    return 100*(float(m)/n)

def dna_to_rna(dna):
    return (dna.replace('T','U'))
