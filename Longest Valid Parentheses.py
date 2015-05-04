class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        m, stack, L = [0]*len(s), [], []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    j = stack.pop()
                    m[i], m[j] = 1, 1
        #tricky :)
        reduce(lambda x,y: x*y+y if not L.append(x*y+y) else 0, m, 0)
        return max(L) if s else 0
