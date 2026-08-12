class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            res += str(len(w)) + "#" + w
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        num = 0
        while i < len(s):
            if s[i] == "#":
                res.append(s[i+1: i+1+num])
                i += num + 1
                num = 0
                continue
            num = (num * 10) + int(s[i])
            i += 1
        return res
