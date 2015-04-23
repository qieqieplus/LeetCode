class Solution:
    # @param s, a string
    # @param p, a string
    # @return a boolean
    def isMatch(self, s, p):
        if len(p) < 2:
            if len(s) is 1 and p is '.':
                return True;
            return s is p;
        if p[1] is '*':
            return self.tryMatch(p[0], s, p[2:])
        if s != '' and (p[0] is s[0] or p[0] is '.'):
            return self.isMatch(s[1: ], p[1: ])
        return False

    def tryMatch(self, ch, text, pattern):
        index = 0
        while True:
            if self.isMatch(text[index: ], pattern):
                return True
            if text != '' and (text[index] is ch or ch is '.'):
                index+=1
            else:
                break
        return False
