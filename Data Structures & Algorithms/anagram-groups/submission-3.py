class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = dict()
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in ana_dict:
                ana_dict[sorted_string] = []
            ana_dict[sorted_string].append(string)
        out_array = []
        for key, val in ana_dict.items():
            out_array.append(val)
        return out_array