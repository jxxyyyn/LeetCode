class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        i = 0
        while i < len(nums) - 1 :
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        
        nums.sort(reverse=True)
        
        if len(nums) < 3:
            return max(nums)
        else:
            return nums[2]