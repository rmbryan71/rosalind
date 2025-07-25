import os

# See my article about this code: https://www.robertbryan.net/posts/2025-07-15-dna.html

def count_nucleotides(sequence):
    return (
        sequence.count("A"),
        sequence.count("C"),
        sequence.count("G"),
        sequence.count("T")
    )


def read_dna_sequence(file_path):
    try:
        with open(file_path, 'r') as dna_file:
            return dna_file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find DNA file: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading DNA file: {e}")


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_dna.txt"
    solution_path = "../solution-outputs/rosalind_dna.txt"
    sequence = read_dna_sequence(file_path)
    a, c, g, t = count_nucleotides(sequence)
#    if os.path.exists(solution_path):
#        os.remove(solution_path)
    file = open(solution_path, "x")
    file.write(f"{a} {c} {g} {t}")
    file.close()
    print(f"{a} {c} {g} {t}")
