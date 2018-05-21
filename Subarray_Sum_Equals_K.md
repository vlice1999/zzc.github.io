## 题目描述
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
```
Input:nums = [1,1,1], k = 2
Output: 2
```
## 解题思路
①暴力搜索法O(N*N)②map容器O(2*N)
## C++(490ms)
```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int re=0,tem;
        for(int i=0;i<nums.size();i++)
        {
            tem=0;
            for(int j=i;j<nums.size();j++)
            {
                tem+=nums[j];
                if(tem==k)re++;
            }
        }
        return re;
    }
};
```
## C++(45ms)
```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int re=0,sum=0;
        map<int,int>rec;
        rec[0]++;//此时代表sum刚好等于k
        for(int i=0;i<nums.size();i++)
        {
            sum+=nums[i];
            re+=rec[sum-k];//rec[sum-k],代表之前的和中有多少sum-k,即符合条件。
            rec[sum]++;
        }
        return re;
    }
};
```
