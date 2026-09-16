class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # This is a clear hashmap problem
        # Iterate through s and t and construct hashmaps
        # showing how many of each letter are in each
        # Then compare the 2

        # This should be and O(n) time and space solution
        # Also, len(s) == len(t) is an assumption
        # ADENDUM: Nevermind they actually have a testcase where the lens are different
        # I thought that was in the constraints, maybe I'm reading them wrong
        if len(s) != len(t):
            return False
        s_dict = dict()
        t_dict = dict()
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        return s_dict == t_dict 