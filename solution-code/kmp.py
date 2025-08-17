from Bio import SeqIO


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_kmp.txt"
    solution_path = "../../solution-outputs/rosalind_kmp.txt"
    sequence_collection = []
    for seq_record in SeqIO.parse(file_path, "fasta"):
        sequence_collection.append(seq_record.seq)
    sequence = sequence_collection.pop(0)
    result = [0]*len(sequence)
    position = 2
    condition = 0
    while position < len(sequence):
        if sequence[position-1]==sequence[condition]:
            condition+=1
            result[position] = condition
            position+=1
        elif condition>0:
            condition=result[condition]
        else:
            result[position]=0
            position+=1
    solution = str((result[1:], 0))
    print((solution).replace('(', '').replace("[",'').replace(',','').replace(']','').replace(')',''))