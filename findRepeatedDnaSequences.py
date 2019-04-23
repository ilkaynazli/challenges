"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = collections.Counter()
        for i in range(len(s)):
            counter[s[i:i+10]] += 1
        
        res = []
        for k, v in counter.items():
            if v > 1:
                res.append(k)
        
        return res