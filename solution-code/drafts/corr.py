import os
from Bio import SeqIO
from Bio.Seq import Seq

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def hamm(a, b):
    solution = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            solution += 1
    # print(a, b, solution)
    return solution

def find_bad_reads(seqs):
    good_reads = []
    bad_reads = []
    for s in seqs:
        bad_reads.append(s)
    for i in range(len(seqs)):
        for j in range(len(seqs)):
            if i != j:
                if seqs[i] == seqs[j]:
                    if i not in good_reads:
                        good_reads.append(i)
                if seqs[i] == Seq.reverse_complement(seqs[j]):
                    if i not in good_reads:
                        # print(sequences[i], " is the reverse complement of ", sequences[j])
                        good_reads.append(i)
    good_reads.sort(reverse = True)
    for k in good_reads:
        del bad_reads[k]
    return bad_reads

def find_good_reads(seqs):
    good_reads = []
    result = []
    for i in range(len(seqs)):
        for j in range(len(seqs)):
            if i != j:
                if seqs[i] == seqs[j]:
                    if i not in good_reads:
                        good_reads.append(i)
                if seqs[i] == Seq.reverse_complement(seqs[j]):
                    if i not in good_reads:
                        # print(sequences[i], " is the reverse complement of ", sequences[j])
                        good_reads.append(i)
    for k in good_reads:
        result.append(seqs[k])
    return result

def corrections(errors, corrects):
    for a in range(len(corrects)):
        corrects.append(Seq.reverse_complement(corrects[a]))
    # print(corrects)
    response = {}
    for s in errors:
        for t in corrects:
            if hamm(s, t) == 1:
                # print(s, "->", t)
                response.update({s: t})
    return response

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_corr.txt"
    solution_path = "../solution-outputs/rosalind_corr.txt"
    if os.path.exists(solution_path):
        os.remove(solution_path)
    sequences = []
    for record in read_fasta(file_path):
        sequences.append(record.seq)
    # print(sequences)
    # print(find_bad_reads(sequences))
    # print(find_good_reads(sequences))
    answer = corrections(find_bad_reads(sequences), find_good_reads(sequences))
    for x, y in answer.items():
        print(x, "->", y)