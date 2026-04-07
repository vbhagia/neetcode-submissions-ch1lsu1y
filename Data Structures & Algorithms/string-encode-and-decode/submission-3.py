class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += string + "'"
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        new_str = ""
        for x in range(len(s)):
            if s[x] == "'":
                output.append(new_str)
                new_str = ""
            else:
                new_str += s[x]
        return output