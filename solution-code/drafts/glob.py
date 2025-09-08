from Bio import SeqIO
from Bio.Align import substitution_matrices
from Bio import Align

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_glob_sample.txt"
    s = str(read_fasta(file_path)[0].seq).strip()
    t = str(read_fasta(file_path)[1].seq).strip()
    print(s, t)
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -5
    aligner.extend_gap_score = -5
    alignments = aligner.align(s, t)
    for alignment in sorted(alignments):
        print(alignment.score)