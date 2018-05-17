## 题目描述
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:
```
Input: [1,3,4,2,2]
Output: 2
```
Example 2:
```
Input: [3,1,3,4,2]
Output: 3
```
## 解题思路
这个题，之前好像做过一个类似的。就是让对应下标处的元素为负数，再找到一个元素是负数的时候返回就可以了。
## C++(10ms)
```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        for(int i=0;i<nums.size();i++)
        {
            if(nums[abs(nums[i])]<0)
                return abs(nums[i]);
            nums[abs(nums[i])]=-nums[abs(nums[i])];
        }
    }
};
```
