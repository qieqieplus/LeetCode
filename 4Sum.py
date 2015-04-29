class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        return self.kSum(num, target, 4)

    # assume num is sorted
    def kSum(self, num, target, k):
        result, num = [], num[:]
        while num:
            #print num, target, k
            head = num.pop(0)
            kMinusSum = self.kSum(num, target-head, k-1) if k>3 else self.twoSum(num, target-head)
            if kMinusSum:
                for sub_index in kMinusSum:
                    seq = [head] + sub_index
                    if seq not in result:
                        result.append(seq)
            while num and num[0] == head:
                num.pop(0)
        return result

    def twoSum(self, num, target):
        map, result, tmp = {}, [], []
        for n in num:
            if n in map:
                if n not in tmp:
                    result.append([target-n, n])
                    tmp.append(n)
            else:
                map[target - n] = True
        return result
