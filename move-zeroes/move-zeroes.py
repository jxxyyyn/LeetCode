class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        
        for j in range(1, len(nums)) :
                if nums[j] != 0 and nums[i] == 0:
                    nums[i], nums[j] = nums[j], nums[i]
                if nums[i] != 0 :
                    i += 1
        
        