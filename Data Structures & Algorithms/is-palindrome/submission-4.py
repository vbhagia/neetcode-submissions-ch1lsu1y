class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pointers to the start and end of the string
        a = 0
        b = len(s) - 1
        # check if the chars are not the same,
        # iterate until b - a <= 1
        while b - a >= 1:
            if not s[a].isalnum():
                a += 1
                continue
            if not s[b].isalnum():
                b -= 1
                continue
            if s[a].lower() != s[b].lower():
                return False
            a = a + 1
            b = b - 1
        return True