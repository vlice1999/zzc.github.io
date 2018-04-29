## 题目描述
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

```
Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```
## 解题思路
这个题说白了就是找数组中是否存在某个数。但是这一串数字的特点是一段有序数字经过了一次翻转后得到的。也就是说可以用中序查找的方式进行，从中间向两边查找。如果中间数字比开头结尾都小，如果目标数字比开头大，比中间数字小，那么目标数字在中间数字左边，否则中间数字右边。如果中间数字比开头结尾都大，目标数字比中间数字大，比结尾数字小，那么目标数字在中间数字右边，否则在左边。特别想吐槽一句，这个题其实毫无存在感，无论是for循环还是vector查找都可以很快的解决。
## C++(6ms)
```cpp
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        if(nums.size()==0)return false;
        int start=0;
        int end=nums.size()-1;
        int pos;
        while(start<=end)
        {
            pos=(start+end)/2;
            if(nums[pos]==target)
                return true;
            if(nums[pos]>nums[start] || nums[pos]>nums[end])
            {
                if(nums[start]<=target && target<nums[pos])
                    end=pos-1;
                else
                    start=pos+1;
            }
            else if(nums[pos]<nums[start] || nums[pos]<nums[end])
            {
                if(nums[pos]<target && target<=nums[end])
                    start=pos+1;
                else
                    end=pos-1;
            }
            else
                end--;
        }
        return false;
    }
};
```
## C++(7ms)
```cpp
//vector
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        vector<int>::iterator it;
        it=find(nums.begin(),nums.end(),target);
        if(it==nums.end())
            return false;
        return true;
    }
};
```
## C++(8ms)
```cpp
//for 循环
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        for(int i=0;i<nums.size();i++)
            if(target==nums[i])
                return true;
        return false;
    }
};
```
