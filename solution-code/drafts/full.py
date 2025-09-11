mydict= {
"A": 71.03711,
"C": 103.00919,
"D": 115.02694,
"E": 129.04259,
"F": 147.06841,
"G": 57.02146,
"H": 137.05891,
"I": 113.08406,
"K": 128.09496,
"L": 113.08406,
"M": 131.04049,
"N": 114.04293,
"P": 97.05276,
"Q": 128.05858,
"R": 156.10111,
"S": 87.03203,
"T": 101.04768,
"V": 99.06841,
"W": 186.07931,
"Y": 163.06333
}

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_full.txt"
    file = open(file_path, "r").readlines()

    rounded_dict = dict()
    for key in mydict:
        rounded_dict[key] = round(mydict[key], 2)

    L = []
    for line in file:
        L.append(float(line.strip()))

    parent_mass = L.pop(0)
    L = sorted(L)
    print(L)
    result = []
    w2 = L.pop(len(L)//2)
    w1 = L.pop(0)
    for a in range(len(L)//2):
        result.append(0)
    print(result)
    print(w1, w2, L)
    prefix, suffix = 0, 0
    for i in range(0, len(L)//2):
        prefix_candidate = L[i] - prefix - w1
        suffix_candidate = L[len(L)//2 + i] - suffix - w2
        if round(prefix_candidate, 2) in rounded_dict.values():
            result[i]=(round(prefix_candidate, 2))
            prefix += prefix_candidate
        if round(suffix_candidate, 2) in rounded_dict.values():
            result[i] = (round(suffix_candidate, 2))
            suffix += suffix_candidate

    for j in result:
        # print(j)
        print(list(rounded_dict.keys())[list(rounded_dict.values()).index(j)], end='')

