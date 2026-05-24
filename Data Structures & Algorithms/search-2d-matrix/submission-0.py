class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = -1
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                target_row = i
                break
        if target_row == -1:
            return False
        l, r = 0, len(matrix[target_row])
        while l <= r:
            m = (l + r) // 2
            if target == matrix[target_row][m]:
                return True
            if target > matrix[target_row][m]:
                l = m + 1
            elif target < matrix[target_row][m]:
                r = m - 1
        return False