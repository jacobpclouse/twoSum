# Leetcode Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        # Flag to set if we found our solution
        foundIndex = 'false'
        
        # while loop exits when flag is true
        while foundIndex == 'false':
            
            # get next test index
            currentIndex1 = nums.pop()
            
            # Getting length of array
            arrayLen = len(nums)
            
            # getting index of last value, will be same as array length
            #currentIndex1 = nums[-1]
            positionOfIndex1 = arrayLen
            
            # finding value needed for other index
            valueNeededForIndex2 = target - currentIndex1
            
            # matching agains other values
            for sillyItem in nums:
                
                # if its a match, get indexes and return them and set flag
                if (sillyItem == valueNeededForIndex2):
                    
                    # getting second index
                    positionOfIndex2 = nums.index(sillyItem)
                    
                    # crafting output
                    outputArray = [positionOfIndex1,positionOfIndex2]
                    
                    # set flag to exit loop
                    foundIndex = "true"
        
        return outputArray
                    
