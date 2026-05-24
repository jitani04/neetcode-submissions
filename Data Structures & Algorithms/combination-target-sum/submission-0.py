class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr_subset = []

        def dfs(i: int, sum: int):
            if sum == target:
                res.append(curr_subset.copy())
                return
            if sum > target or i >= len(nums):
                return        
            sum += nums[i]
            curr_subset.append(nums[i])
            dfs(i, sum)

            sum -= nums[i]
            curr_subset.pop()
            dfs(i + 1, sum)

        dfs(0, 0)
        return res

