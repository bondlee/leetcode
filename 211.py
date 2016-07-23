# coding: utf-8
# Created by bondlee on 2016/6/25


class WordDictionary(object):

    class Node(object):
        def __init__(self):
            self.child = {}
            self.leaf = 0

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = self.Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.trie
        for i in word:
            if i not in cur.child:
                cur.child[i] = self.Node()
            cur = cur.child[i]
        cur.leaf = 1

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(r, cur):
            if res[0]:
                return
            if r == len(word) and cur.leaf:
                res[0] = 1
            if r < len(word):
                if word[r] != "." and word[r] in cur.child:
                    dfs(r+1, cur.child[word[r]])
                if word[r] == ".":
                    for i in cur.child.iterkeys():
                        dfs(r+1, cur.child[i])
        res = [0]
        dfs(0, self.trie)
        return res[0] == 1


if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("word")
    print wordDictionary.search("wor.")