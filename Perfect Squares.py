import math

class Solution(object):
    def numSquares(self, n):
        sqNum = [ i * i for i in range(1, int(math.sqrt(n)) + 1) ]
        return 1 if n in sqNum else self.recursive([n], sqNum, 1)

    def recursive(self, numbers, square, depth):
        result = []
        for n in numbers:
            for s in square:
                if n > s:
                    if n - s in square:
                        return depth + 1
                    result.append(n - s)
        return self.recursive (result, square, depth + 1)
