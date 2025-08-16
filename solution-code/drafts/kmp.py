from Bio import SeqIO

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_kmp.txt"
    solution_path = "../solution-outputs/rosalind_kmp.txt"
    sequence = str(read_fasta(file_path)[0].seq)
    print(sequence)
    result = []
    for i in range(1, len(sequence)):
        if i == 1:
            result.append(0)
        if sequence[i]!=sequence[0]:
            result.append(0)
        else:
            result.append(1)
            value = 1
            while sequence[i+value] == sequence[value]:
                value+=1
                result.append(value)
    print(result)