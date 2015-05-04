class Solution:
    # @param s, a string
    # @param p, a string
    # @return a boolean
    def isMatch(self, s, p):
        if len(p) < 2:
            return True if (len(s) == 1 and p == '.') else s == p

        if p[1] == '*':
            #optimization for rare cases
            offset = 2
            while offset+1 < len(p) and p[offset] == p[0] and p[offset+1] == '*':
                offset += 2
            return self.tryMatch(p[0], s, p[offset:])

        if s != '' and (p[0] == s[0] or p[0] == '.'):
            return self.isMatch(s[1: ], p[1: ])

        return False

    def tryMatch(self, ch, text, pattern):
        index, length = 0, len(text)
        while True:
            if self.isMatch(text[index: ], pattern):
                return True
            if index < length and (ch == text[index] or ch == '.'):
                index += 1
            else:
                break
        return False
