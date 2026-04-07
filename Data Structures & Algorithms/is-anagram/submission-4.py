class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if strings are same length
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
