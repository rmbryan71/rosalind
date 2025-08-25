from Bio import SeqIO

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

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
    au_pairs = max(mydict['A'], mydict['U'])
    cg_pairs = max(mydict['C'], mydict['G'])
    return au_pairs * cg_pairs

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_mmch.txt"
    s = str(read_fasta(file_path)[0].seq).strip()
    print(count_max_matchings(s))
