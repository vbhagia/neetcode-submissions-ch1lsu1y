class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Easiest way to know if we have an anagram is to sort.
        # This would take O(m log(m) n) time, dominated by sort.
        # Putting them together after in arrays is trivial, and linear.
        # Of course, space would be O(n)    

        # We could also find anagrams by using a hashmap. This is faster, but requires more space.
        # In total, time: O(m * n), space: O(m * n)
        
        # Let's just sort first idk
        dic = dict()
        # The schema of this dict will be:
        # Key: the sorted string to compare against (so we know if we have an anagram or not)
        # Value: an array of strings in strs that meet this criteria
        for string in strs:
            sorted_string = ''
            for char in sorted(string):
                sorted_string += char
            if sorted_string in dic:
                dic[sorted_string].append(string)
            else:
                dic[sorted_string] = [string]
        print(dic)

        # Now we need to create the array for outputting from this dict
        output = []
        for group in dic:
            output.append(dic[group])

        return output
                        