class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        def generator(pList, k, df):
            if k == n:
                return [p + ')'*df for p in pList]
            if df == 0:
                return generator([p + '(' for p in pList], k+1, df+1)
            return generator([p + '(' for p in pList], k+1, df+1)\
                 + generator([p + ')' for p in pList], k, df-1)
        return generator([''], 0, 0)
#print Solution().generateParenthesis(5)