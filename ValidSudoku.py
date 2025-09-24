class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:  
        temp = []        
        for i in range(1, 10): 
            temp.clear()
            for m in range(((i - 1) // 3) * 3, ((i - 1) // 3) * 3 + 3):            
                for n in range (((i - 1) % 3) * 3, ((i - 1) % 3) * 3 + 3):
                    if board[m][n] != ".":
                        temp.append(board[m][n])
            for m in range (len(temp)):
                for n in range (len(temp)):
                    if m != n:
                        if temp[n] != ".":
                            if temp[m] == temp[n]:                            
                                return False
        temp = [".", ".", ".", ".", ".", ".", ".", ".", "."]
        for m in range (9):
            for n in range (9):
                temp[n] = board[m][n]
            for i in range (9):
                for n in range (9):
                    if i != n:
                        if temp[i] != ".":
                            if temp[i] == board[m][n]:
                                return False
        for n in range (9):
            for m in range (9):
                temp[m] = board[m][n]
            for i in range (9):
                for m in range (9):
                    if i != m:
                        if temp[i] != ".":
                            if temp[i] == board[m][n]:
                                return False
        return True