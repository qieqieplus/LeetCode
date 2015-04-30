class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        for i in range(len(num)-1, 0, -1):
            if num[i-1] < num[i]:
                for j in range(len(num)-1, i-1, -1):
                    if num[i-1] < num[j]:
                        num[i-1], num[j] = num[j], num[i-1]
                        num[i:] = num[i:][::-1]
                        return
        num.reverse()
        #return num