class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        map={}
        for i in range(len(num)):
            if num[i] in map:
                return (map[num[i]]+1, i+1)
            map[target - num[i]] = i