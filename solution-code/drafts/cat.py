from Bio import SeqIO

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)

def cat(n):
    if n == 0:
        return 1
    else:
        return 2*(2*n-1) * cat(n-1)/(n+1)

def maxchar(s):
    return max(s.count("A"), s.count("G"))

def isComplement(a, b):
    if a == "A" and b == 'U' or a == 'U' and b == 'A':
        return True
    if a == "C" and b == 'G' or a == 'G' and b == 'C':
        return True
    else:
        return False

def pairings(s):
    result = []
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if isComplement(s[i], s[j]):
                result.append([i, j] + pairings(s[:i]+s[i+1:j]+s[j+1:]))
    return result

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_cat_figure3.txt"
    s = str(read_fasta(file_path)[0].seq).strip()
    nodes = []
    for char in s:
        nodes.append(char)
    print(len(pairings(nodes)))


