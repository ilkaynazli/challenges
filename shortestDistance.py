"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

"""

class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        location = {word1:[], word2:[]}
        
        for i, word in enumerate(words):
            if word == word1:
                location[word1].append(i)
            elif word == word2:
                location[word2].append(i)
        
        min_dist = len(words)
        for index1 in location[word1]:
            for index2 in location[word2]:
                min_dist = min(min_dist, abs(index1-index2))
 
        return min_dist