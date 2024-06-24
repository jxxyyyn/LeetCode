class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)== 0 :
            return -1
        
        largest = max(nums)
        largest_index = nums.index(largest)
        
        for num in nums:
            if num != largest and largest < 2 * num:
                return -1
        
        return largest_index