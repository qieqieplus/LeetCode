class Solution:
    # @param x, an integer
    # @return an integer
    def reverse(self, x):
        result, symbol = 0, 1
        if x < 0:
            symbol, x = -1, -x
        while x:
            result = result * 10 + x % 10
            x /= 10
        return result * symbol if result <= (0x7FFFFFFF) else 0
