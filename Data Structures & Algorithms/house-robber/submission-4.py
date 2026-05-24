class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            else:
                memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2)) 
                #separates into 2 branches, skip current house (i + 1)
                # or rob current house and continue to next possible house
            return memo[i]
        return dfs(0)