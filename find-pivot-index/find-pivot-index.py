class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = sum(nums)
        temp = 0
        
        for i in range(len(nums)) : 
            if nums[i] == total - 2*temp : 
                return i
            temp += nums[i]
        
        return -1
        
        
        
