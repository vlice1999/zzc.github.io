## 题目描述
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k. 

一个给定的数组nums，判断该数组中是否存在这样的数对满足| nums[i] - nums[j] | <= t 且 | i - j | <= k.
## 题目分析
用了两种方法，一种是直接两个for循环，时间复杂度O(n*n)；第二种是暂存一个k长度的数组，排序后检查这个数组相邻两个元素的差值是否小于t，时间复杂度O(k*n),也超时了。还没能想出更好的解决方案……
## 失败代码（python）
```python
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k==0:
            return False
        for i in range(len(nums)):
            temp=nums[i:min(len(nums),i+k+1)]
            temp.sort()
            for j in range(len(temp)-1):
                if temp[j+1]-temp[j]<=t:
                    return True
        return False
```
