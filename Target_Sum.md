## 题目描述
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.
```
Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
```
##　解题思路
递归遍历所有的组合，找到Ｓ,re+1返回
## C++(661ms)
```cpp
class Solution {
private:
    int re=0;
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        helper(nums,0,0,S);
        return re;
    }
    void helper(vector<int>& nums,int start,int tem,int S)
    {
        if(start==nums.size())
        {if(tem==S)
                re++;}
        else if(start<nums.size())
        {
            helper(nums,start+1,tem+nums[start],S);
            helper(nums,start+1,tem-nums[start],S);
        }
    }
};
```
## C++(27ms)
```cpp
//别人的动态规划解决方案
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int re[2001]={0};
        int now[2001]={0};
        re[1000]=1;
        for(int i=0;i<nums.size();i++)
        {
            for(int j=0;j<2001;j++)
                if(re[j]!=0)
                {
                    now[j+nums[i]]+=re[j];
                    now[j-nums[i]]+=re[j];
                }
            for(int j=0;j<2001;j++)
            {
                re[j]=now[j];
                now[j]=0;
            }
        }
        if(S>1000)
            return 0;
        return re[S+1000];
    }
};
```
