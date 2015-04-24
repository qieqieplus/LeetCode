class Solution:
    # @param s, a string
    # @return a string
    def longestPalindrome(self, s):
        # S = "abba", T = "^#a#b#b#a#$"
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            #print(i, C, R, P[i])
            P[i] = min(R-i, P[2*C -i]) if R > i else 0 # equals to i' = C - (i-C)
            while T[i +P[i] +1] == T[i -P[i] -1]:
                P[i] +=1

            if i +P[i] > R:
                C, R = i, i +P[i]
                if R == n-2:
                    break;
        maxLen, center = max((n, i) for i, n in enumerate(P))
        return s[(center -maxLen)//2 : (center +maxLen)//2]

#    def longestPalindrome(self, s):
#        if len(s) < 2:
#            return s
#        if len(s) is 2:
#            return s if s[0]==s[1] else s[0]
#        longest = Node(s,0,0)
#        for i in range(0, len(s)-1):
#            if s[i] is s[i+1]:
#                current = Node(s, i, i+1)
#                current.extend()
#                if current.length > longest.length:
#                    longest = current
#                    if longest.length == len(s):
#                        return longest.getStr()
#        for i in range(0, len(s)-2):
#            if s[i] is s[i+2]:
#                current = Node(s, i, i+2)
#                current.extend()
#                if current.length > longest.length:
#                    longest = current
#                    if longest.length == len(s):
#                        return longest.getStr()
#        return longest.getStr()
#
#class Node:
#    def __init__(self, str, start, end):
#        self.str = str
#        self.start = start
#        self.end = end
#        self.length = end-start+1
#    def extend(self):
#        while (self.start>0 and self.end<len(self.str)-1 and \
#            self.str[self.start-1] is self.str[self.end+1]):
#            self.start -=1
#            self.end +=1
#        self.length = self.end-self.start+1
#    def getStr(self):
#        return self.str[self.start: self.end+1]
