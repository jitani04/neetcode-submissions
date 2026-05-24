class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        seq_len = 1
        max_seq = 1
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        for i in range((len(nums) - 1), 0, -1):
            if nums[i] == nums[i - 1] + 1:
                seq_len += 1
                max_seq = max(seq_len, max_seq)
            elif nums[i] == nums[i -1]:
                continue
            else:
                seq_len = 1
        return max_seq