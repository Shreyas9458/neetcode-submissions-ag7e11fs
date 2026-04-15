class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for word in strs:
            encodedString += str(len(word)) + "#" + word
        # print(encodedString)
        return encodedString
        

    def decode(self, s: str) -> List[str]:
        result = list()
        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            result.append(s[i + 1: i + 1 + int(length)])
            i += int(length) + 1
        return result

            

