class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L=len(nums)
        step=nums[0]
        if L==1:
            return True
        for i in range(1,L):
            if step<i:
                return False
            step=max(step,nums[i]+i)
            if step>=L-1:
                return True
