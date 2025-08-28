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
    file_path = "/Users/robertbryan/Downloads/rosalind_spec.txt"
    file = open(file_path, "r").readlines()

    rounded_dict = dict()
    for key in mydict:
        rounded_dict[key] = round(mydict[key], 2)
    # print(rounded_dict)

    L = []
    for line in file:
        L.append(float(line.strip()))
    for i in range(1, len(L)):
        j = round((L[i] - L[i-1]), 2)
        print(list(rounded_dict.keys())[list(rounded_dict.values()).index(j)], end='')
