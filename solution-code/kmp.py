from Bio import SeqIO

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_kmp.txt"
    for record in SeqIO.parse(file_path, "fasta"):
        sequence = record.seq
    result = [-1]
    counter = -1
    for i in range(len(sequence)):
        while counter >= 0 and sequence[i] != sequence[counter]:
            counter = result[counter]
        counter += 1
        result.append(counter)
    print(*result[1:])