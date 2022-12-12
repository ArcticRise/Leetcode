"""
Tries or PrefixTries are an efficent data structure that is mostly used for retrivial of strings, some applications that it is used for is autocomplete and spellchecker, etc

Runtime for the trie is usally O(M) where M is the length of the key!!

"""

class TrieNode():

    def __init__(self) -> None:
        self.children = [None]*26
        self.isEnd = False

class Trie():

    def __init__(self) -> None:
        self.root = TrieNode()
    
    #Insert the word into the trie
    def insert(self, word: str) -> None:
        curNode = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curNode.children[index]:
                curNode.children[index] = TrieNode()
            curNode = curNode.children[index]
        curNode.isEnd = True

    #Check if the word exist in the trie, return true if exist false otherwise
    def search(self, word: str) -> bool:
        curNode = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curNode.children[index]:
                return False
            curNode = curNode.children[index]
        return curNode.isEnd


my_trie = Trie()
my_trie.insert("Hello")
my_trie.insert("Michael")
print(my_trie.search("What"))
print(my_trie.search("Michael"))
    
