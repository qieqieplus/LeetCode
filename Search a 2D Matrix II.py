class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        x, y = 0, m

        while x <= n and y>=0:
        	if matrix[y][x] > target:
        		y -= 1
        	elif matrix[y][x] < target:
        		x += 1
        	else:
        		return True
        return False
