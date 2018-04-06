## 题目描述
```
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Note: The solution set must not contain duplicate quadruplets.
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```
## 题目描述
先记录每两个数相加所得和及下标（放到字典中），然后再重复一次操作。不同于2Sum与3Sum，这个题不适用线性时间算法，因为无法先固定某一个元素。
## Python(209ms)
```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        dic={}
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                num=nums[i]+nums[j]
                if num in dic:
                    dic[num].append([i,j])
                else:
                    dic[num]=[[i,j]]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)-2):
                temp=target-nums[i]-nums[j]
                if temp in dic:
                    for k in dic[temp]:
                        if k[0]>j and [nums[i],nums[j],nums[k[0]],nums[k[1]]]not in result:
                            result.append([nums[i],nums[j],nums[k[0]],nums[k[1]]])
        return result
```
## C++(59ms)
```cpp
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        vector<vector<int>>re;
        unordered_map<int,vector<pair<int,int>>> dic;
        int temp=0;
        if(nums.size()<4)return re;
        for(int i=0;i<nums.size()-1;i++)
        {
            for(int j=i+1;j<nums.size();j++)
            {
                temp=nums[i]+nums[j];
                dic[temp].push_back(pair<int,int>(i,j));
            }
        }
        for(int i=0;i<nums.size()-1;i++)
        {
            if(i>0&&nums[i]==nums[i-1])continue;
            for(int j=i+1;j<nums.size();j++)
            {
                if(j>i+1&&nums[j]==nums[j-1])continue;
                temp=target-nums[i]-nums[j];
                if(dic.find(temp)!=dic.end())
                {
                    vector<pair<int,int>>sum=dic[temp];
                    bool is=true;
                    for(int k=0;k<sum.size();k++)
                    {
                        if(sum[k].first<=j)continue;
                        if(is==true||(re.back())[2]!=nums[sum[k].first])
                        {
                            vector<int>re_temp{nums[i],nums[j],nums[sum[k].first],nums[sum[k].second]};
                            re.push_back(re_temp);
                            is=false;
                        }
                    }
                }
            }
        }
        return re;
    }
};
```
