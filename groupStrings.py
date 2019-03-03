"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def decode(s):
            key = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14, 'p':15, 'q':16,'r':17,'s':18,'t':19, 'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
            temp = []
            for char in s:
                temp.append(key[char])
                
            dec = temp[0]
            for i in range(len(temp)):
                temp[i] -= dec
                temp[i] = temp[i] % 26
                temp[i] = str(temp[i])
            
                
            return '-'.join(temp)
        
        d = {}
        for s in strings:
            decoded = decode(s)
            if decoded in d:
                d[decoded].append(s)
            else:
                d[decoded] = [s]
        
        res = list(d.values())
        return res