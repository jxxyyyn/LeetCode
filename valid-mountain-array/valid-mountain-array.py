class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        i = 0
        j = len(arr) - 1
        
        if len(arr) < 3 :
            return False
            
        while i+1 < j and arr[i] < arr[i+1] : 
            i += 1
        while 0 < j-1 and arr[j] < arr[j-1] : 
            j -= 1
                
        return i == j