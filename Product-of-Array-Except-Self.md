## 题目描述
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Solve it without division and in O(n).
For example, given [1,2,3,4], return [24,12,8,6]. 
给一串数组，返回这串数字除他自身外的数的乘积
## 解题思路
从左往右遍历一次得到当前数左边的数字之积，从右往左遍历一次得到当前数字右边的数字之积。
## C++(54ms)
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len,t=1;
        len=nums.size();
        vector<int> re;
        for(int i=0;i<len;i++)
            re.push_back(1);
        for(int i=0;i<len-1;i++)
        {
            t*=nums[i];
            re[i+1]=t;
        }
        t=1;
        for(int i=len-1;i>=0;i--)
        {
            t*=nums[i];
            re[i-1]*=t;
        }
        return re;
    }
};
```
## Python(185ms)
```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        re=[1]*len(nums)
        t=1
        for i in range(len(nums)-1):
            t*=nums[i]
            re[i+1]=t
        t=1
        i=len(nums)-1
        while i>0:
            t*=nums[i]
            re[i-1]*=t
            i-=1
        return re
```
