class Solution:
    delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + self.delimiter + string
        return encoded
    def decode(self, s: str) -> List[str]:
        buf = ""
        strs = []
        length = 0
        pos = 0
        while pos < len(s):
            if s[pos] != self.delimiter:
                buf += s[pos]
                pos += 1
            else:
                length = int(buf)
                buf = ""
                # put the string in buf and add that to strs
                i = 0
                i += 1
                pos += 1
                while i <= length:
                    buf += s[pos]
                    i += 1
                    pos += 1
                strs.append(buf)
                buf = ""
        return strs