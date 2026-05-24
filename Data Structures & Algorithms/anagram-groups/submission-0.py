class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for str in strs:
            ordered_string = "".join(sorted(str))
            if ordered_string in seen:
                seen[ordered_string].append(str)
            else:
                seen[ordered_string] = [str]
        res = list(seen.values())
        return res