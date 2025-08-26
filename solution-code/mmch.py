from Bio import SeqIO

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)

def count_bases(s):
    dict = {'A':0, 'U':0, 'G':0, 'C':0}
    for char in s:
        dict[char] += 1
    return dict

def len_max_matchings(s):
    mydict = (count_bases(s))
    au_pairs = min(mydict['A'], mydict['U'])
    cg_pairs = min(mydict['C'], mydict['G'])
    return au_pairs+cg_pairs

def count_max_matchings(s):
    mydict = (count_bases(s))
    au_max = max(mydict['A'], mydict['U'])
    au_min = min(mydict['A'], mydict['U'])
    cg_max = max(mydict['C'], mydict['G'])
    cg_min = min(mydict['C'], mydict['G'])
    au_count = fact(au_max) // fact(au_max-au_min)
    cg_count = fact(cg_max) // fact(cg_max-cg_min)
    return au_count*cg_count

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_mmch.txt"
    s = str(read_fasta(file_path)[0].seq).strip()
    print(count_max_matchings(s))
    print(len(s))
