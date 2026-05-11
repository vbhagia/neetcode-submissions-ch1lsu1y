class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Now let's just use a hashmap (This would be O(n) time and O(n) space)

        # We build a hashmap for s
        seen_s = dict()
        for letter in s:
            seen_s[letter] = seen_s.get(letter, 0) + 1

        # Now we tear it town in t.
        # If we run into something not there, return False
        # If the dict is not empty by the end, return False

        print(f"dict before done:\n{seen_s}")

        for letter in t:
            try:
                if seen_s[letter] > 0:
                    seen_s[letter] -= 1
                else:
                    return False
            except KeyError: #Letter not there
                return False
        
        print(f"dict after done:\n{seen_s}")
        
        for key in seen_s:
            if seen_s[key] != 0:
                return False
        return True