class Solution:
    def isPalindrome(self, s: str) -> bool:
    # 2 pointer approach
    # time: O(n), space: O(n)
    # start with l and r at the ends
    # skip non-alphanums
    # check s[l] == s[r] while l < r
        l = 0
        r = len(s) - 1
        while l <= r:
            # check for alphanums
            if s[l].isalnum() == False:
                l += 1
                continue
            if s[r].isalnum() == False:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True