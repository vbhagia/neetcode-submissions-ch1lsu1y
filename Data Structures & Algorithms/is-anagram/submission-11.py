class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Hashmap approach will be O(n) time and O(n) space
        s_map = dict()
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        
        t_map = dict()
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        return s_map == t_map
        
            
