class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        dic = {
            '1':'',     '2':'abc',   '3':'def',
            '4':'ghi',  '5':'jkl',   '6':'mno',
            '7':'pqrs', '8':'tuv',   '9':'wxyz'
        }

        def add(a, b):
            return [ x+y for x in a for y in dic[b] ]

        return reduce (add, digits, ['']) if digits else []

#print Solution().letterCombinations('')