from os.path import expanduser
home = expanduser('~')
import math


# with open('./datasets/rosalind_prob_example.txt') as f:
#     s = f.readline()
#     myList = f.readline().split(' ')


with open(expanduser('~/Downloads/rosalind_prob.txt')) as f:
    s = f.readline()
    myList = f.readline().split(' ')


# dataset = (read_fasta('./datasets/rosalind_prob_example.txt'))
# dataset = (read_fasta('./datasets/rosalind_sseq.txt'))
# dataset = (read_fasta(expanduser('~/Downloads/rosalind_sseq.txt')))

#print(s)
#print(*myList)

def helper(c, k):
    '''Given a char (c) and a float(k), return likelihood of randomly generating c if k is the G/C content'''
    if c == 'A' or c == 'T':
        return (1 - k)/2
    else:
        return (k / 2)

for j in myList:
    chance = 1
    for i in s.strip():
        chance *= (helper(i, float(j)))
    print(round(math.log10(chance), 3), end=' ')