class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        length = 0
        i = 0
        while i < len(s):
            if s[i] == "#":
                decoded.append(s[i+1:i+1+length])
                i = i + 1 + length
                length = 0
            else:
                length = length * 10 + int(s[i])
                i += 1
        return decoded
