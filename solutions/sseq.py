# Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
#
# Return: One collection of indices of s in which the symbols of t appear
# as a subsequence of s. If multiple solutions exist, you may return any one.

import Bio.SeqIO

from os.path import expanduser
home = expanduser('~')


def read_fasta(fasta_file):
    '''Read fasta file and return the list of records, consisting of
    description and sequence'''
    handle = open(fasta_file)
    records = list(Bio.SeqIO.parse(handle, "fasta"))
    handle.close()
    return [(str(rec.seq)) for rec in records]


# dataset = (read_fasta('./datasets/rosalind_sseq_example.txt'))
# dataset = (read_fasta('./datasets/rosalind_sseq.txt'))
dataset = (read_fasta(expanduser('~/Downloads/rosalind_sseq.txt')))
s = dataset[0]
t = dataset[1]

#print(s, t)

# print(s[3])

result = []
bookmark = 0
final = []

for symbol in t:
    result.append(s.find(symbol, bookmark))
    bookmark = s.find(symbol, bookmark) + 1

for number in result:
    final.append(number + 1)

print(final)

with open('./results/rosalind_sseq_results.txt', 'w') as f:
    #f.write(''.join(str(final)).strip())
    f.write(' '.join(map(str, final)))
