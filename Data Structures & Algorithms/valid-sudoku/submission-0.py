class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        subBoxes = defaultdict(set)
        digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in rows[i]:
                    return False
                elif board[i][j] in digits:
                    rows[i].add(board[i][j])
        
        for j in range(len(board[0])):
            for i in range(len(board)):
                if board[i][j] in columns[j]:
                    return False
                elif board[i][j] in digits:
                    columns[j].add(board[i][j])
        for i in range(len(board)):
            for j in range(len(board[0])):
                #floor division rounds down to the nearest whole integer
                if board[i][j] in subBoxes[i // 3, j //3]:
                    return False
                elif board[i][j] in digits:
                    subBoxes[i // 3, j // 3].add(board[i][j])
        return True
                