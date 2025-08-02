import os
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def read_protein_sequence(file_path):
    try:
        with open(file_path, 'r') as protein_file:
            return protein_file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find Protein file: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading Protein file: {e}")

def prtm(file_path):
    seq = ProteinAnalysis(read_protein_sequence(file_path), True)
    # print(seq.sequence)
    return seq.molecular_weight() - 18.01056

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_prtm.txt"
    solution_path = "../solution-outputs/rosalind_prtm.txt"
    solution = str(prtm(file_path))
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(solution)
    file.close()
    print(solution)