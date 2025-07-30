from Bio.Seq import Seq

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_orf.txt"
    sequence = ''.join(x.strip() for x in open(file_path, 'r').readlines()[1:])
    sequence1 = str(Seq(sequence).reverse_complement())
    # print(sequence)
    # print('\n')
    # print(sequence1)

    dna = []
    for i in range(0, len(sequence)):
        if sequence[i:i+3] == 'ATG':
            dna.append(sequence[i:])
        if sequence1[i:i+3] == 'ATG':
            dna.append(sequence1[i:])
    # print(dna)

    proteinlist = []
    for j in dna:
        protein = Seq(j).translate()
        if protein.find('*') != -1:
            proteinlist.append(str(protein[:protein.find('*')]))
    # print(proteinlist)

    print('\n'.join(y for y in list(set(proteinlist))))

