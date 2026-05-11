class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort them both and compare (O(n log(n)) due to the sort times)
        return sorted(s) == sorted(t)