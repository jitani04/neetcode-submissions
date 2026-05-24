class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count, product = 0, 1
        for num in nums: 
            if num == 0: 
                zero_count += 1
                continue
            else:
                product *= num
        res = []
        for num in nums:
            if zero_count > 1 or (zero_count == 1 and num != 0):
                res.append(0)
            elif num == 0 and zero_count == 1:
                res.append(product)
            elif zero_count == 0 and num != 0:
                res.append(product//num)
            
        return res 
        