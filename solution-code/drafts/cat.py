from Bio import SeqIO
import itertools

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
    if a == 'A' and b == 'U':
        return True
    if a == 'U' and b == 'A':
        return True
    if a == 'C' and b == 'G':
        return True
    if a == 'G' and b == 'C':
        return True
    else:
        return False

def matches(s):
    s = list (s)
    # print(s)
    matches = []
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j:
                if isComplement(s[i], s[j]):
                    # print(i, j, s[i], s[j])
                    if [j, i] not in matches:
                        matches.append([i,j])
    return matches

def is_complete_match(s):
    s = list (s)
    for i in range(len(s)-1):
        x = s[i][0]
        y = s[i][1]
        for j in range(i+1, len(s)):
            if s[j][0] == x or s[j][1] == x:
                return False
            if s[j][0] == y or s[j][1] == y:
                return False
    return True

def remove_dupes(s, x, y):
    response = []
    for edge in s:
        if edge[0] != x and edge[1] != x and edge[0] != y and edge[1] != y:
            response.append(edge)
    return response

def fast_complete_matches(s):
    nodes = []
    for char in s:
        nodes.append(char)
    match_set = matches(nodes)
    complete_matches = []
    for match in match_set:
        # print(match)
        subset = [[match] + remove_dupes(match_set, match[0], match[1])]

    return complete_matches

def slow_complete_matches(s):
    nodes = []
    for char in s:
        nodes.append(char)
    complete_matches = []
    for subset in itertools.combinations(matches(nodes), len(nodes)//2):
        if is_complete_match(subset):
            complete_matches.append(subset)
    return complete_matches

def is_noncrossing(t):
    t = list(t)
    for edge_pair in itertools.combinations(t, 2):
        i = int(edge_pair[0][0])
        j = int(edge_pair[0][1])
        k = int(edge_pair[1][0])
        l = int(edge_pair[1][1])
        # print(i, j, k, l)
        if i < k < j < l:
            return False
        if j < k < i < l:
            return False
        if i > k > j > l:
            return False
        if j > k > i > l:
            return False
        if j < l < i < k:
            return False
    return True


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_cat_figure3.txt"
    s = str(read_fasta(file_path)[0].seq).strip()
    nodes = []
    for char in s:
        nodes.append(char)
    # print(matches(nodes))
    # print(count_complete_edges(matches(nodes)))
    # print(complete_matches(matches(nodes), []))
    print(slow_complete_matches(s))
    print(len(slow_complete_matches(s)))
    print(fast_complete_matches(s))



