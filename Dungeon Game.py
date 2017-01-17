class Solution(object):

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        matrix = [[0 for i in range(n)] for j in range(m)]
        visted = [[0 for i in range(n)] for j in range(m)]
        result = -1048576;
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    matrix[i][j] = dungeon[0][0]
                elif i == 0 and j > 0:
                    matrix[i][j] = dungeon[i][j] + matrix[i][j-1]
                elif j == 0 and i > 0:
                    matrix[i][j] = dungeon[i][j] + matrix[i-1][j]
                elif i == m and j == n:
                    matrix[i][j] = dungeon[i][j] + max(matrix[i][j-1], matrix[i-1][j])

        print matrix, life
        if matrix[m-1][n-1] > 0:
            return 1
        else:
            return 2 - life[m-1][n-1]

    def push(self, dungeon, x, y):

dungeon = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]

dungeon = [
    [1,-2,3],
    [2,-2,-2]
]


s = Solution()
print s.calculateMinimumHP(dungeon)

[
    [-2, -5, 2],
    [-7, -15, 3],
    [3, 15]
 ]
[
    [2, 0, 3],
    [4, 2, 1]
 ]