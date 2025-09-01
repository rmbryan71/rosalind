def mink_diff(S1, S2):
    result = []
    for s1 in S1:
        for s2 in S2:
            result.append(round(s1 - s2, 5))
    return result

def max_multiplicity(mylist):
    item = max(mylist, key=mylist.count)
    return mylist.count(item)

def max_diff(mylist):
    newlist = []
    for item in mylist:
        newlist.append(abs(item))
    return max(newlist, key=newlist.count)

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_conv.txt"
    S1 = []
    S2 = []
    x = open(file_path).readlines()
    for value in x[0].split(' '):
        S1.append(float(value))
    for value2 in x[1].split(' '):
        S2.append(float(value2))
    # print(S1, S2)
    mydiff = mink_diff(S1, S2)
    print(max_multiplicity(mydiff))
    print(max_diff(mydiff))
