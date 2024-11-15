
# In searching algorithms, a trie (pronounced “try”) is a type
# of tree data structure used to efficiently store and retrieve keys,
# often strings, with a focus on performance in search operations.
# It is also known as a prefix tree because it enables fast lookups
# based on the prefixes of words or sequences. Tries are especially
# useful for tasks like autocomplete systems, spell checkers,
# or dictionary applications where you need to find words based on prefixes.

# Structure of a Trie
# 1.	Nodes and Edges: Each node in a trie represents a character of a key, and edges represent connections between characters. The root node is typically empty, and each child node corresponds to the next character in a word.
# 2.	Paths for Words: Each path from the root to a node represents a prefix of one or more words. The nodes collectively store all prefixes of the inserted words.
# 3.	End of Word Markers: To indicate the end of a word, nodes often have a flag or marker.
class TrieNode:
    def __init__(self):
        # Each node contains a dictionary to store children and a boolean to mark the end of a word
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        # The root of the trie is an empty TrieNode
        self.root = TrieNode()

    def insert(self, word):
        # Start from the root
        node = self.root
        for char in word:
            # If character is not in the current node's children, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # Mark the end of the word
        node.is_end_of_word = True

    def search(self, word):
        # Start from the root
        node = self.root
        for char in word:
            # If the character isn't in the node's children, word doesn't exist
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # Check if this node marks the end of the word
        return node.is_end_of_word

    def starts_with(self, prefix):
        # Check if there is any word that starts with the given prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Usage example
trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("dog")

# Searching for words
print(trie.search("cat"))      # Output: True
print(trie.search("car"))      # Output: True
print(trie.search("dog"))      # Output: True
print(trie.search("bat"))      # Output: False

# Checking prefixes
print(trie.starts_with("ca"))  # Output: True
print(trie.starts_with("do"))  # Output: True
print(trie.starts_with("ba"))  # Output: False