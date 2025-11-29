#An anagram is a word or phrase formed from the same letters of another word or phrase in a different order. For example, the word "CAT" can be rearranged to create the anagram "CATALOG" or "CATS". Anagrams are often used in puzzles, games, and literature to create new words or phrases from existing ones
"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
"""

"""
first solution to come up with is an two arrays of words and counting of each size and compairing them but as bigger word longer time complexity
but firstly ve should check len of words

 class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        alphabet = [0] * 26 #making empty 26 symp az eng alphab
        for x in range(len(s)):
            alphabet[ord(s[x]) - ord('a')] += 1
            alphabet[ord(t[x]) - ord('a')] -= 1
        for val in alphabet:
            if val != 0:
                return False
        return True

        from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars, t_chars = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            s_chars[s[i]] += 1
            t_chars[t[i]] += 1

        return s_chars == t_chars

  o(s + t) time 
  o(s + t) mem




  
  """
