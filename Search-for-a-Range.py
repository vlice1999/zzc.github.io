class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1=0
        index2=0
        l=len(nums)-1
        i=0
        while i<l+1:
            if nums[i]<target:
                i+=1
            else:
                index1=i
                break
        while l>=0:
            if nums[l]>target:
                l-=1
            else:
                index2=l
                break
        if target not in nums:
            return [-1,-1]
        return [index1,index2]
