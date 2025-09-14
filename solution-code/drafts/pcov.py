from Bio import SeqIO
import sys, os

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def min(a, b):
    return a if a < b else b

def overlap(str1, str2):
    max_len = -sys.maxsize
    len1 = len(str1)
    len2 = len(str2)
    str_ = ""
    for i in range(1, min(len1, len2) + 1):
        if str1[len1-i:] == str2[:i]:
            if max_len < i:
                max_len = i
                str_ = str1 + str2[i:]
    for i in range(1, min(len1, len2) + 1):
        if str1[:i] == str2[len2-i:]:
            if max_len < i:
                max_len = i
                str_ = str2 + str1[i:]
    return max_len, str_

def long(arr, n):
    while n != 1:
        max_len = -sys.maxsize
        l, r = 0, 0
        res_str = ""
        for i in range(n):
            for j in range(i+1, n):
                str_ = ("")
                res, str_ = overlap(arr[i], arr[j])
                if max_len < res:
                    max_len = res
                    res_str = str_
                    l, r = i, j
        n -= 1
        if max_len == -sys.maxsize:
            arr[0] += arr[n]
        else:
            arr[l] = res_str
            arr[r] = arr[n]
    return arr[0]

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_pcov.txt"
    reads = []

