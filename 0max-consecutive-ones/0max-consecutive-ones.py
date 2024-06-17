class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0
        temp = 0
        for i in range(len(nums)) :
            if nums[i] == 1 :
                temp += 1
            else :
                maximum = max(temp, maximum)
                temp = 0
        return max(temp, maximum)
                