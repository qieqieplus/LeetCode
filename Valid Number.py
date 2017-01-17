import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        digit2 = re.compile("^[\ ]*[+-]?(\d+\.?\d*|\d*\.?\d+)(e[+-]?\d+)?[\ ]*$")
        
        return bool(digit2.match(s))

s = Solution()
print s.isNumber('0xFF')