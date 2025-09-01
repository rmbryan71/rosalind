

def LCSLength(s, t):
    C = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                C[i][j]=C[i-1][j-1] + 1
            else:
                C[i][j]=max(C[i][j-1], C[i-1][j])
    return C


def backtrack(C, s, t, i, j):
    if i == -1:
        return ""
    if j == -1:
        return ""
    if s[i] == t[j]:
        return backtrack(C, s, t, i-1, j-1) + s[i]
    if C[i][j-1] > C[i-1][j]:
        return backtrack(C, s, t, i, j-1)
    else:
        return backtrack(C, s, t, i-1, j)

def scsp(s, t, lcs):
    i = 0
    j = 0
    scs = []
    for char in lcs:
        while s[i] != char:
            scs.append(s[i])
            i += 1
        while t[j] != char:
            scs.append(t[j])
            j += 1
        scs.append(char)
        i += 1
        j += 1
    scs.extend(list(s[i:]))
    scs.extend(list(t[j:]))
    return "".join(scs)

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_scsp_sample.txt"
    strings = []
    x = open(file_path).readlines()
    s = x[0].strip()
    t = x[1].strip()
    print(s, t)
    lcs = (backtrack((LCSLength(s, t)), s, t, len(s)-1, len(t)-1))
    print(scsp(s, t, lcs))
