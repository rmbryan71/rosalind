from os.path import expanduser
home = expanduser('~')
import math
import Bio.SeqIO


# with open('./datasets/rosalind_prob_example.txt') as f:
#     s = f.readline()
#     myList = f.readline().split(' ')


# with open(expanduser('~/Downloads/rosalind_tran.txt')) as f:
#     s = f.readline()
#     myList = f.readline().split(' ')

dataset = []

with open('./datasets/rosalind_tran_example.txt') as f:
    for record in Bio.SeqIO.parse(f, 'fasta'):
        dataset.append(record.seq)

#dataset = (Bio.SeqIO.read('./datasets/rosalind_tran_example.txt', format=fasta))
# dataset = (read_fasta('./datasets/rosalind_sseq.txt'))
# dataset = (read_fasta(expanduser('~/Downloads/rosalind_sseq.txt')))

s1 = str(dataset[0])
s2 = str(dataset[1])

print(len(s1), len(s2))