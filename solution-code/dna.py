def count_nucleotides(sequence):
    """
    Count the occurrences of each nucleotide in a DNA sequence.

    Args:
        sequence (str): A DNA sequence string containing A, C, G, and T nucleotides

    Returns:
        tuple: Count of (A, G, C, T) nucleotides in the sequence
    """
    return (
        sequence.count("A"),
        sequence.count("C"),
        sequence.count("G"),
        sequence.count("T")
    )


def read_dna_sequence(file_path):
    """
    Read DNA sequence from a file.

    Args:
        file_path (str): Path to the file containing DNA sequence

    Returns:
        str: The DNA sequence read from the file
    """
    try:
        with open(file_path, 'r') as dna_file:
            return dna_file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find DNA file: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading DNA file: {e}")


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_dna.txt"
    sequence = read_dna_sequence(file_path)
    a, c, g, t = count_nucleotides(sequence)
    file = open("../solution-outputs/rosalind_dna.txt", "x")
    file.write(f"{a} {c} {g} {t}")
    file.close()
