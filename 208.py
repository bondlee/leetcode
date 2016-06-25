# coding: utf-8
# Created by bondlee on 2016/6/25


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.leaf = 0


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.leaf = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for i in word:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return False
        return cur.leaf == 1


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for i in prefix:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

if __name__ == '__main__':
    trie = Trie()
    trie.insert("abc")
    print trie.search("abc")
    print trie.search("ab")
    print trie.startsWith("a")
    trie.insert("ab")
    print trie.search("ab")
    pass