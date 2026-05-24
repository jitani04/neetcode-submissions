class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            ordered_string = "".join(sorted(s))
            if ordered_string in seen:
                seen[ordered_string].append(s)
            else:
                seen[ordered_string] = [s]
        res = list(seen.values())
        return res