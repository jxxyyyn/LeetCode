class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        expected = sorted(heights)
        wrong = 0
        
        for i in range(len(heights)) :
            if heights[i] != expected[i]:
                wrong += 1
                
        return wrong