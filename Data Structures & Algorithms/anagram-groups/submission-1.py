class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Hashmap stores alphabetized entries, and index in output list
        output = []
        seen = dict()
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) in seen:
                #add strs[i] to the corresponding sublist in output
                output[seen[''.join(sorted(strs[i]))]].append(strs[i])
            else:
                #add sorted(strs[i]) to the hashmap
                seen[''.join(sorted(strs[i]))] = len(output)
                #add strs[i] to a new sublist in output
                output.append([strs[i]])
        return output