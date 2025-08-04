def performReversal(sequence, start, end):
    prefix = sequence[:start]
    reversed_subsequence = sequence[start:end][::-1]
    suffix = sequence[end:]
    return prefix + reversed_subsequence + suffix

def findBreakpoints(sequence, target_sequence):
    breakpoints = []
    for i in range (len(sequence)-1):
        current_element = sequence[i]
        adjacent_element = sequence[i+1]
        if abs(target_sequence.index(current_element) - target_sequence.index(adjacent_element)) != 1:
            breakpoints.append(i+1)
    return breakpoints

def findMinimumBreakpointReversals(sequences, target_sequence):
    reversals = []
    for sequence in sequences:
        breakpoints = findBreakpoints(sequence, target_sequence)
        for start_i in range(len(breakpoints)-1):
            for end_i in range(start_i+1, len(breakpoints)):
                reversals.append(performReversal(sequence, breakpoints[start_i], breakpoints[end_i]))
    min_bp = len(target_sequence)
    minium_reversals = []
    for reversal in reversals:
        num_breakpoints = len(findBreakpoints(reversal, target_sequence))
        if num_breakpoints < min_bp:
            min_bp = num_breakpoints
            minium_reversals = [reversal]
        elif num_breakpoints == min_bp:
            minium_reversals.append(reversal)
    return minium_reversals

def getReversalDistance(sequence, target_sequence):
    sequence = ["-"] + sequence + ["+"]
    target_sequence = ["-"] + target_sequence + ["+"]
    reversals = 0
    current_sequences = [sequence]
    while target_sequence not in current_sequences:
        current_sequences = findMinimumBreakpointReversals(current_sequences, target_sequence)
        reversals += 1
    return reversals

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_rear.txt"
    solution_path = "../../solution-outputs/rosalind_rear.txt"

    with open(file_path) as file:
        d = [line.strip() for line in file.readlines()]
    res = [[int(x) for x in line.split(" ")] for line in d if line]
    dist = [getReversalDistance(res[i], res[i+1]) for i in range(0, len(res), 2)]
    print(str(dist).strip("[]").replace(",", ""))