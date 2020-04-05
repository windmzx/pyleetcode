class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root={}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p=self.root
        for s  in word:
            if s in p.keys():
                p=p[s]
            else:
                p[s]={}
                p=p[s]
        p['isword']=True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p=self.root
        for s in word:
            if s in p.keys():
                p=p[s]
            else:
                return False
        if "isword" in p.keys():
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p=self.root
        for s in word:
            if s in p.keys():
                p=p[s]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)