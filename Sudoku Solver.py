from collections import Counter

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        maxLoop = 30
        while maxLoop:
            maxLoop, flag = maxLoop-1, 0
            for i in range(0, 9):
                for j in range(0, 9):
                    if board[i][j] == '.':
                        s = self.search(board, [i, j])
                        if maxLoop == 1:
                            print(s)
                        if len(s) == 1:
                            board[i][j] = s[0]
                        else:
                            flag = 1
                if maxLoop == 1:
                    print("==========")
            if flag == 0:
                break
        c = Counter()
        for line in board:
            c.update(line)
        del c["."]
        print (c)
        return board

    def search(self, board, pos):
        [x, y] = pos
        vars = []
        for i in range(0, 9):
            if board[i][y] != '.':
                vars.append(board[i][y])
        for j in range(0, 9):
            if board[x][j] != '.':
                vars.append(board[x][j])
        x, y = x - x%3, y- y%3
        for i in range(x, x+3):
            for j in range(y, y+3):
                if board[i][j] != '.':
                    vars.append(board[i][j])
        return self.diff(vars)

    def diff(self, ls):
        return [i for i in '123456789' if i not in ls]

ln = 9
input = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board = [[0]*9]*9
for line in range(0, ln):
    board[line] = [i for i in input[line]]
s = Solution()
print(s.solveSudoku(board))
a