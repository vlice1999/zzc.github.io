class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print nums
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[len(nums)-1]!=nums[len(nums)-2]:
            return nums[len(nums)-1]
        i=1
        while i<len(nums)-1:
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]
            i+=1
