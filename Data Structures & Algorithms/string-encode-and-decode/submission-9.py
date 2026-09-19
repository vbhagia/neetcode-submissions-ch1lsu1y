class Solution:
    delimiter = "@"

    def encode(self, strs: List[str]) -> str:
        # Turn the list of strings into a single string
        # Whose form is <length: int><delimiter><string>
        s = ""
        for string in strs:
            s += str(len(string)) + self.delimiter + string
        return s




    def decode(self, s: str) -> List[str]:
        # need a buffer to read each char into
        # need an array to place output strings
        # Decode will work in the follwoing manner:
        # Step 1: Read length until delimiter.
        # Assign length as what's in the buffer, flush the buffer
        # Step 2: read <length> chars past the delimiter into the buffer
        # Step 3: append what's in the buffer to the output array as a string.
        # Step 4: Flush the buffer
        # Step 5: repeat until there are no more chars in the encoded string
        buf = ""
        output = []
        
        i = 0
        length = 0
        while i < len(s):
            if s[i] == self.delimiter:
                # Whatever is in buf is the length
                length = int(buf)
                buf = ""

                # Now but the string in the buffer
                i += 1
                for j in range(length):
                    buf += s[i + j]
                i += length

                # add the string to the output and repeat
                output.append(buf)
                buf = ""
            
            else:
                buf += s[i]
                i += 1
        return output
            