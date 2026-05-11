class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Now let's just use a hashmap (This would be O(n) time and O(n) space)

        # We build a hashmap for both s and t and compare the two.
        seen_s = dict()
        for letter in s:
            seen_s[letter] = seen_s.get(letter, 0) + 1
        
        seen_t = dict()
        for letter in t:
            seen_t[letter] = seen_t.get(letter, 0) + 1
        
        return seen_s == seen_t