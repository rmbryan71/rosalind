import os

def read_rna_sequence(file_path):
    try:
        with open(file_path, 'r') as dna_file:
            return dna_file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find DNA file: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading DNA file: {e}")

RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}


def codon_frequencies():
    frequencies = {}
    for k, v in RNA_CODON_TABLE.items():
        # print(k, v)
        if not v in frequencies:
            frequencies[v] = 0
        frequencies[v] += 1
    # print (frequencies)
    return frequencies



### Solving code goes here
def mrna(file_path):
    input = read_rna_sequence(file_path)
    f = codon_frequencies()
    n = f.get("Stop")

    for c in input:
        n *= f.get(c)
        n %= 1000000 # do the mod every loop

    return str(n)
### End of solving code

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_mrna.txt"
    solution_path = "../solution-outputs/rosalind_mrna.txt"
    if os.path.exists(solution_path):
        os.remove(solution_path)
    file = open(solution_path, "x")
    file.write(mrna(file_path))
    file.close()
    print(mrna(file_path))