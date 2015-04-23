class Solution:
    # @return a string
    def convert(self, s, nRows):
        result = ''
        if nRows <= 1: return s
        T = nRows-1
        r = [[] for i in range(nRows)]
        for n in range(len(s)):
            i = abs(n%(2*T)-T)
            r[T - i] += s[n]
        for item in r:
            result += ''.join(item)
        return result