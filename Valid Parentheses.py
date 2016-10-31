class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        before, parens = '', ['()', '[]', '{}']
        while s:
            before = s
            for pair in parens:
                s = self.reduce(s, pair)
            if len(s) == len(before):
                return False    
        return True
    
    def reduce(self, str, chars):
        l = len(chars);
        while True:
            pos = str.find(chars);
            if pos == -1:
                return str;
            str = str[:pos] + str[pos+l:];
