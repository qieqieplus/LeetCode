class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        result = []
        while num:
            target = num.pop(0)
            twoSum = self.twoSum(num, -target)
            if twoSum:
                for sub_index in twoSum:
                    result.append([target] + sub_index)
            while num and num[0] == target:
                num.pop(0)
        return result

    def twoSum(self, num, target):
        map={}
        result, tmp = [], []
        for n in num:
            if n in map:
                if n not in tmp:
                    result.append([target-n, n])
                    tmp.append(n)
            else:
                map[target - n] = True
        return result
