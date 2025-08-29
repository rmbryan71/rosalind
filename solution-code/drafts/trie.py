class TrieNode:
    def __init__(self, text = ''):
        self.text = text
        self.children = dict()

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]

    def __child_words_for(self, node, words):
        '''
        Private helper function. Cycles through all children
        of node recursively, adding them to words if they
        constitute whole words (as opposed to merely prefixes).
        '''
        if node.is_word:
            words.append(node.text)
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)

    def starts_with(self, prefix):
        '''
        Returns a list of all words beginning with the given prefix, or
        an empty list if no words begin with that prefix.
        '''
        words = list()
        current = self.root
        for char in prefix:
            if char not in current.children:
                # Could also just return words since it's empty by default
                return list()
            current = current.children[char]

        # Step 2
        self.__child_words_for(current, words)
        return words

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_trie_sample.txt"
    file = open(file_path, "r").readlines()
    strings = []
    for line in file:
        strings.append(line.strip())
    print(strings)
    trie = PrefixTree()
    for string in strings:
        trie.insert(string)
    print(trie.starts_with(''))