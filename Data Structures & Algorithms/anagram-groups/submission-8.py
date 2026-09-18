class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We can iterate through strs,
        # and construct hashmap signatures for each string.
        # We can then take those signatures, and match them in a hashmap
        # The hashmap should have structure key: <alphabetized str>,
        # val: <array of every instance of this anagram>

        # This Solution is:
        # Time complexity: O(n * m).
        # Where n is the number of strings in strs,
        # and m is the length of a single string
        # Space complexity: O(n * m)

        strmap = dict()

        for s in strs:
            sorted_s = sorted(s)
            s_sorted = ""
            for char in sorted_s:
                s_sorted += char
            
            if s_sorted in strmap:
                strmap[s_sorted].append(s)
            else:
                strmap[s_sorted] = [s]
        
        output = []
        
        for key, value in strmap.items():
            output.append(value)
        
        return output