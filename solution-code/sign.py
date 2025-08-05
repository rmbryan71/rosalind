from itertools import permutations
from itertools import product

list1 = [-1, 1]
list2 = [-2, 2]
list3 = [-3, 3]
list4 = [-4, 4]
list5 = [-5, 5]
list6 = [-6, 6]


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_sign.txt"
    solution_path = "../../solution-outputs/rosalind_sign.txt"
    result = []
    with open(file_path) as file:
        x = int(file.readline())
    firstlist = list(product(list1, list2, list3))
    secondlist = []
    for item in firstlist:
        secondlist.append(list(permutations(item)))
    for item in secondlist:
        for i in item:
            result.append(i)
    print(len(result))
    for answer in result:
        print(str(answer).replace('(', '').replace(')', '').replace(',',''))