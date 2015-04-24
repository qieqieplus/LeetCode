class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        distance = target - nums[0] - nums[1]- nums[2]
        for n in range(len(nums)):
            i, j = n+1, len(nums)-1
            while i < j:
                threeSum = nums[n] + nums[i] + nums[j]
                if threeSum == target:
                    return threeSum
                
                if abs(target - threeSum) < abs(distance):
                    distance = target - threeSum

                if  threeSum < target:
                    i += 1
                else:
                    j -= 1

        return target - distance

#    def twoSumClosest(self, nums, target):
#        nums.sort()
#        i, j = 0, len(nums)-1
#        distance = target - nums[i] - nums[j]
#        while i < j:
#            twoSum = nums[i] + nums[j]
#            if twoSum == target:
#                return twoSum
#            
#            if abs(target - twoSum) < abs(distance):
#                distance = target - twoSum
#
#            if  twoSum < target:
#                i += 1
#            else:
#                j -= 1
#        return target - distance
