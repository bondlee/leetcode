# coding: utf-8
# Created by bondlee on 2016/6/25


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.trie
        for i in word:
            if i not in cur:
                cur = {}
                cur[i] = {}
            cur = cur[i]

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        ind = 0
        wl = len(word)
        while ind < wl:
            w = word[ind]
            if w != ".":
                ind += 1

if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("word")
    wordDictionary.search("pattern")