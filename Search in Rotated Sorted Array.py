class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #cheat
        try:
            index = nums.index(target)
        except ValueError:
            index = -1
        return index
