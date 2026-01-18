class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def getsqr(x,y):
            match x:
                case 8:
                    match y:
                        case 8:
                            return [board[6][6], board[6][7], board[7][6], board[7][7]]
                        case 7:
                            return [board[6][6], board[6][8], board[7][6], board[7][8]]
                        case 6:
                            return [board[6][7], board[6][8], board[7][7], board[7][8]]
                        case 5:
                            return [board[6][3], board[6][4], board[7][3], board[7][4]]
                        case 4:
                            return [board[6][3], board[6][5], board[7][3], board[7][5]]
                        case 3:
                            return [board[6][4], board[6][5], board[7][4], board[7][5]]
                        case 2:
                            return [board[6][0], board[6][1], board[7][0], board[7][1]]
                        case 1:
                            return [board[6][0], board[6][2], board[7][0], board[7][2]]
                        case 0:
                            return [board[6][1], board[6][2], board[7][1], board[7][2]]
                case 7:
                    match y:
                        case 8:
                            return [board[6][6], board[6][7], board[8][6], board[8][7]]
                        case 7:
                            return [board[6][6], board[6][8], board[8][6], board[8][8]]
                        case 6:
                            return [board[6][7], board[6][8], board[8][7], board[8][8]]
                        case 5:
                            return [board[6][3], board[6][4], board[8][3], board[8][4]]
                        case 4:
                            return [board[6][3], board[6][5], board[8][3], board[8][5]]
                        case 3:
                            return [board[6][4], board[6][5], board[8][4], board[8][5]]
                        case 2:
                            return [board[6][0], board[6][1], board[8][0], board[8][1]]
                        case 1:
                            return [board[6][0], board[6][2], board[8][0], board[8][2]]
                        case 0:
                            return [board[6][1], board[6][2], board[8][1], board[8][2]]
                case 6:
                    match y:
                        case 8:
                            return [board[7][6], board[7][7], board[8][6], board[8][7]]
                        case 7:
                            return [board[7][6], board[7][8], board[8][6], board[8][8]]
                        case 6:
                            return [board[7][7], board[7][8], board[8][7], board[8][8]]
                        case 5:
                            return [board[7][3], board[7][4], board[8][3], board[8][4]]
                        case 4:
                            return [board[7][3], board[7][5], board[8][3], board[8][5]]
                        case 3:
                            return [board[7][4], board[7][5], board[8][4], board[8][5]]
                        case 2:
                            return [board[7][0], board[7][1], board[8][0], board[8][1]]
                        case 1:
                            return [board[7][0], board[7][2], board[8][0], board[8][2]]
                        case 0:
                            return [board[7][1], board[7][2], board[8][1], board[8][2]]
                case 5:
                    match y:
                        case 8:
                            return [board[3][6], board[3][7], board[4][6], board[4][7]]
                        case 7:
                            return [board[3][6], board[3][8], board[4][6], board[4][8]]
                        case 6:
                            return [board[3][7], board[3][8], board[4][7], board[4][8]]
                        case 5:
                            return [board[3][3], board[3][4], board[4][3], board[4][4]]
                        case 4:
                            return [board[3][3], board[3][5], board[4][3], board[4][5]]
                        case 3:
                            return [board[3][4], board[3][5], board[4][4], board[4][5]]
                        case 2:
                            return [board[3][0], board[3][1], board[4][0], board[4][1]]
                        case 1:
                            return [board[3][0], board[3][2], board[4][0], board[4][2]]
                        case 0:
                            return [board[3][1], board[3][2], board[4][1], board[4][2]]
                case 4:
                    match y:
                        case 8:
                            return [board[3][6], board[3][7], board[5][6], board[5][7]]
                        case 7:
                            return [board[3][6], board[3][8], board[5][6], board[5][8]]
                        case 6:
                            return [board[3][7], board[3][8], board[5][7], board[5][8]]
                        case 5:
                            return [board[3][3], board[3][4], board[5][3], board[5][4]]
                        case 4:
                            return [board[3][3], board[3][5], board[5][3], board[5][5]]
                        case 3:
                            return [board[3][4], board[3][5], board[5][4], board[5][5]]
                        case 2:
                            return [board[3][0], board[3][1], board[5][0], board[5][1]]
                        case 1:
                            return [board[3][0], board[3][2], board[5][0], board[5][2]]
                        case 0:
                            return [board[3][1], board[3][2], board[5][1], board[5][2]]                        
                case 3:
                    match y:
                        case 8:
                            return [board[4][6], board[4][7], board[5][6], board[5][7]]
                        case 7:
                            return [board[4][6], board[4][8], board[5][6], board[5][8]]
                        case 6:
                            return [board[4][7], board[4][8], board[5][7], board[5][8]]
                        case 5:
                            return [board[4][3], board[4][4], board[5][3], board[5][4]]
                        case 4:
                            return [board[4][3], board[4][5], board[5][3], board[5][5]]
                        case 3:
                            return [board[4][4], board[4][5], board[5][4], board[5][5]]
                        case 2:
                            return [board[4][0], board[4][1], board[5][0], board[5][1]]
                        case 1:
                            return [board[4][0], board[4][2], board[5][0], board[5][2]]
                        case 0:
                            return [board[4][1], board[4][2], board[5][1], board[5][2]]
                case 2:
                    match y:
                        case 8:
                            return [board[0][6], board[0][7], board[1][6], board[1][7]]
                        case 7:
                            return [board[0][6], board[0][8], board[1][6], board[1][8]]
                        case 6:
                            return [board[0][7], board[0][8], board[1][7], board[1][8]]
                        case 5:
                            return [board[0][3], board[0][4], board[1][3], board[1][4]]
                        case 4:
                            return [board[0][3], board[0][5], board[1][3], board[1][5]]
                        case 3:
                            return [board[0][4], board[0][5], board[1][4], board[1][5]]
                        case 2:
                            return [board[0][0], board[0][1], board[1][0], board[1][1]]
                        case 1:
                            return [board[0][0], board[0][2], board[1][0], board[1][2]]
                        case 0:
                            return [board[0][1], board[0][2], board[1][1], board[1][2]]
                case 1:
                    match y:
                        case 8:
                            return [board[0][6], board[0][7], board[2][6], board[2][7]]
                        case 7:
                            return [board[0][6], board[0][8], board[2][6], board[2][8]]
                        case 6:
                            return [board[0][7], board[0][8], board[2][7], board[2][8]]
                        case 5:
                            return [board[0][3], board[0][4], board[2][3], board[2][4]]
                        case 4:
                            return [board[0][3], board[0][5], board[2][3], board[2][5]]
                        case 3:
                            return [board[0][4], board[0][5], board[2][4], board[2][5]]
                        case 2:
                            return [board[0][0], board[0][1], board[2][0], board[2][1]]
                        case 1:
                            return [board[0][0], board[0][2], board[2][0], board[2][2]]
                        case 0:
                            return [board[0][1], board[0][2], board[2][1], board[2][2]]
                case 0:
                    match y:
                        case 8:
                            return [board[1][6], board[1][7], board[2][6], board[2][7]]
                        case 7:
                            return [board[1][6], board[1][8], board[2][6], board[2][8]]
                        case 6:
                            return [board[1][7], board[1][8], board[2][7], board[2][8]]
                        case 5:
                            return [board[1][3], board[1][4], board[2][3], board[2][4]]
                        case 4:
                            return [board[1][3], board[1][5], board[2][3], board[2][5]]
                        case 3:
                            return [board[1][4], board[1][5], board[2][4], board[2][5]]
                        case 2:
                            return [board[1][0], board[1][1], board[2][0], board[2][1]]
                        case 1:
                            return [board[1][0], board[1][2], board[2][0], board[2][2]]
                        case 0:
                            return [board[1][1], board[1][2], board[2][1], board[2][2]]
        false = [False, False, False, False, False, False, False, False, False, False]
        numsx = []
        numsy = []
        empty = []
        for i in range(9):
            numsx.append(false[::])
            numsy.append(false[::])
        for x in range (9):
            for y in range (9):
                if board[x][y] == ".":
                    board[x][y] = 0
                    empty.append([x,y])
                else:
                    board[x][y] = int(board[x][y])
                    numsx[x][board[x][y]] = True
                    numsy[y][board[x][y]] = True
        last = len(empty)
        step = 0
        while step < last:            
            x = empty[step][0]
            y = empty[step][1]            
            start = board[x][y]
            num = start
            if num != 9:
                for searching in range(start + 1,10):
                    have = False
                    if numsx[x][searching] == True or numsy[y][searching] == True:
                        have = True
                    if have == False:
                        sqr = getsqr(x,y)
                        for i in range(4):
                            if sqr[i] == searching:
                                have = True
                                break
                    if have == False:
                        num = searching                    
                        break
            numsx[x][start] = False
            numsy[y][start] = False
            if num != start:  
                numsx[x][num] = True
                numsy[y][num] = True
                board[x][y] = num
                step += 1
            else:
                board[x][y] = 0              
                step -= 1     
        for x in range (9):
            for y in range (9):
                board[x][y] = str(board[x][y])