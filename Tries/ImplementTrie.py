"""
LeetCode [208]: Implement Trie (Prefix Tree)

Design a trie (pronounced as "try") or prefix tree with the following operations:

1. insert(word): Inserts the string word into the trie.
2. search(word): Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
3. startsWith(prefix): Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Approach:
Implement a TrieNode class to represent each node in the trie. Each TrieNode will contain a dictionary mapping characters to their corresponding child nodes and a boolean flag indicating if it marks the end of a word. Then, implement the Trie class with insert, search, and startsWith methods.

Code with Comments:
"""

class TrieNode:
    def __init__(self):
        # Initialize the children dictionary to store child nodes
        self.children = {}
        # Initialize the end of word flag to False
        self.eow = False

class Trie:
    def __init__(self):
        # Initialize the root of the trie with an empty TrieNode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Initialize the current node as the root
        curr = self.root
        # Iterate through each character in the word
        for char in word:
            # Check if the current character exists as a child node
            if char not in curr.children:
                # If the character does not exist, create a new TrieNode for it
                curr.children[char] = TrieNode()
            # Move to the next node
            curr = curr.children[char]
        # Mark the end of the word
        curr.eow = True

    def search(self, word: str) -> bool:
        # Initialize the current node as the root
        curr = self.root
        # Iterate through each character in the word
        for char in word:
            # Check if the current character exists as a child node
            if char not in curr.children:
                # If the character does not exist, the word is not in the trie
                return False
            # Move to the next node
            curr = curr.children[char]
        # Check if the end of the word flag is set
        return curr.eow

    def startsWith(self, prefix: str) -> bool:
        # Initialize the current node as the root
        curr = self.root
        # Iterate through each character in the prefix
        for char in prefix:
            # Check if the current character exists as a child node
            if char not in curr.children:
                # If the character does not exist, the prefix is not in the trie
                return False
            # Move to the next node
            curr = curr.children[char]
        # The prefix is found in the trie
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
