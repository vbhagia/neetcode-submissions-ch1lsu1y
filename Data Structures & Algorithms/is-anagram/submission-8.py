class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        comp_s = dict()
        comp_t = dict()
        for letter in s:
            comp_s[letter] = comp_s.get(letter, 0) + 1
        for letter in t:
            comp_t[letter] = comp_t.get(letter, 0) + 1
        return comp_s == comp_t
            