
class WordDictionary:

    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        

    def addWord(self, word: str) -> None:
        current = self
        for char in word:
            
            index = ord(char) - 97
            if not current.children[index]:
                current.children[index] = WordDictionary()
            current = current.children[index]
        current.is_end = True
        

    def search(self, word: str) -> bool:
        current = self
        n = len(word)
        for i in range(n):
            char = word[i]
            if char == ".":
                for ch in current.children:
                    if ch and ch.search(word[i+1:]):
                        return True
                return False
            
            index = ord(char) - 97
            if not current.children[index]:
                return False
            current = current.children[index]
        if current.is_end: return True
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)