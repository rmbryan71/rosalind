import sys
from itertools import permutations

def rotations(s):
    result = []
    for i in range(len(s)):
        result.append(s[i:] + s[:i])
    return result

def add_cyclic(s, t):
    if len(s) < len(t):
        return False
    s1 = s + s
    if t in s1:
        return s
    s1 = rotations(s)
    t1 = rotations(t)
    max_overlap = 0
    result = ''
    for s_ in s1:
        for t_ in t1:
            if max_overlap_count(s_, t_) > max_overlap:
                result = concat_strings(s_, t_)
                max_overlap = max_overlap_count(s_, t_)
            if max_overlap_count(t_, s_) > max_overlap:
                result = concat_strings(t_, s_)
                max_overlap = max_overlap_count(t_, s_)
    return result

def max_overlap_count(str1, str2):
    a = len(str1) + len(str2)
    b = len(overlap(str1, str2))
    return int(a-b)


def concat_strings(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return str1 + str2
    for i in range(min(len(str1), len(str2)), 0, -1):
        if str1.endswith(str2[:i]):
            return str1 + str2[i:]
    return str1 + str2

def overlap(str1, str2):
    r1 = len(concat_strings(str1, str2))
    r2 = len(concat_strings(str2, str1))
    if r1 >= r2:
        return concat_strings(str2, str1)
    else:
        return concat_strings(str1, str2)

def pcov(reads):
    response = reads[0]
    for j in range(1, len(reads)):
        response = add_cyclic(response, reads[j])
    return response

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_pcov.txt"
    reads = []
    with open(file_path) as file:
        for line in file:
            reads.append(str(line.strip()))
    print(pcov(reads))

