class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)) :
            if len(str(nums[i])) % 2 == 0 :
                res += 1
        return res