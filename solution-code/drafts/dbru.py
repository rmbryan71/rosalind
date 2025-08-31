def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Create the complement sequence
    comp_seq = ''.join(complement[base] for base in seq)
    # Return the reverse of the complement
    return comp_seq[::-1]

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_dbru.txt"
    file = open(file_path, "r").readlines()
    S = []
    for line in file:
        S.append(line.strip())
    reverse_complements = []
    for sequence in S:
        reverse_complements.append(reverse_complement(sequence))
    for rc in reverse_complements:
        if rc not in S:
            S.append(rc)
    k = len(S[0])-1
    kmers = []
    for string in S:
        kmers.append(string[1:])
        kmers.append(string[:-1])
    # print(kmers)
    count = 0
    for edge in S:
        count += 1
        e = str((edge[:-1], edge[1:]))
        print(e.replace("'", ""))

