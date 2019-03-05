"""
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
"""

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.word_set = set(dictionary)
        self.word_d = self.abb_dict()
    
    def abb_dict(self):
        word_d = {}
        for word in self.word_set:
            temp = self.abb_word(word)
            word_d[temp] = word_d.get(temp, 0) + 1
        return word_d
    
    
    def isUnique(self, word: str) -> bool:
        if word in self.word_set and self.word_d[self.abb_word(word)] < 2:
            return True
        return not self.abb_word(word) in self.word_d
        
        
        
    
    def abb_word(self, word):
        if len(word) < 3:
            return word
        num = len(word) - 2
        return word[0] + str(num) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)