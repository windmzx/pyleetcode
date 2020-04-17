class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree={}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        p=self.tree
        for char in word:
            if char  in p.keys():
                p=p[char]
            else:
                p[char]={}
                p=p[char]
        p['is_word']="#"



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        return self.helper(word,self.tree)
        
    def helper(self,word:str,p):
        if word=="":
            return True
        i=0
        for char in word:
            if char==".":
                for re in p.keys():
                    if re!='is_word':
                        if self.helper(word[1+i:],p[re]):
                            return True
                return False
            elif char in p.keys():
                p=p[char]
                i+=1
            else:
                return False
        return "is_word" in p.keys()



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
if __name__ == "__main__":
    x=WordDictionary()
    # x.addWord("a")
    # x.addWord("a")
    x.addWord("mad")
    x.addWord("bad")
    x.addWord("dad")
    print()
    # print(x.search("pab"))
    # print(x.search("bcd"))
    # print(x.search(".ad"))
    # print(x.search("b.."))
    # print(x.search("."))
    # print(x.search("a"))
    # print(x.search("aa"))
    # print(x.search("a"))
    # print(x.search(".a"))
    print(x.search("b.."))
    print(x.search("bad"))

