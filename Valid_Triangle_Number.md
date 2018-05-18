## 题目描述
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
```
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
```
## 解题思路
①暴力搜索②双指针
## C++(19ms)
```cpp
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int len=nums.size();
        if(len<3)return 0;
        int re=0;
        for(int i=len-1;i>1;i--)
        {
            int left=0,right=i-1;
            while(left<right)
            {
                if(nums[right]+nums[left]>nums[i])
                {
                    re+=(right-left);    
                    right--;
                }
                else
                    left++;
            }
        }
        return re;
    }
};
```
## C++(570ms)
```cpp
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        if(nums.size()<3)return 0;
        int re=0;
        for(int i=0;i<nums.size()-2;i++)
            for(int j=i+1;j<nums.size()-1;j++)
                for(int z=j+1;z<nums.size();z++)
                    if(nums[i]+nums[j]>nums[z])re++;
                    else
                        break;
        return re;
    }
};
```
