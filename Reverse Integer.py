class Solution:
    # @param x, an integer
    # @return an integer
    def reverse(self, x):
        result = 0
        symbol = 1
        if x < 0:
            symbol = -1
            x = -x
        while x:
            result = result * 10 + x % 10
            x /= 10
        return result * symbol if result <= (0x7FFFFFFF) else 0
