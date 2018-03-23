## 题目描述
Given a list of non negative integers, arrange them such that they form the largest number.
For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.
## 解题思路
利用python2中sort()的cmp用法，根据(a+b)和(b+a)大小进行排序。
## Python(56ms)
```python
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(a,b):
            return int(b + a) - int(a + b)
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        nums = sorted(nums,cmp=compare)
        ans = ''.join(nums).lstrip('0') #排除[0,0]这种情况
        return ans or '0'
```
