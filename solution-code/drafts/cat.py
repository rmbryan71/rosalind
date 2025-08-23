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

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_cat_sample2.txt"
    s = str(read_fasta(file_path)[0].seq).strip()
    ls = len(s)
    print(ls)
    print(maxchar(s))
    print(cat()%1000000)

