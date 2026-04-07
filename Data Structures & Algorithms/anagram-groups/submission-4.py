class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = dict()
        for string in strs:
            sorted_string = ""
            for letter in sorted(string):
                sorted_string += letter
            if ana_dict.get(sorted_string) != None:
                ana_dict[sorted_string].append(string)
            else:
                ana_dict[sorted_string] = [string]
        output = []
        for key, val in ana_dict.items():
            output.append(val)
        return output
