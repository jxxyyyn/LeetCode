class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        i = 0
        for j in range(1,len(nums)) :
            if nums[i] % 2 == 1 and nums[j] % 2 == 0 :
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] % 2 == 0:
                i += 1
        
        return nums