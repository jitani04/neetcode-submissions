class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s) + 1) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)
            res.append("".join(s[(i + 1): (i + length)])) 
            i += length
        return res
