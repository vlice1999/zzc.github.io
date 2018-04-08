## 题目描述
```
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

如果S中有a,b,c满足a+b+c==0，返回所有的满足这个条件的[a,b,c]，而且不能重复
```
## 解题思路
S排序，先固定一个元素，然后再双指针分别从固定元素之后的首元素和末元素开始遍历，时间复杂度为O(n^2)
## Python(1258ms)
```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort()
        l=len(nums)
        for i in range(0,l-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=l-1
            if nums[i]>0 or nums[right]<0:
                break
            while left<right and nums[left]+nums[i]<=0:
                s=nums[i]+nums[left]+nums[right]
                if s==0:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:left+=1
                    while left<right and nums[right]==nums[right+1]:right-=1
                elif s>0:
                    right-=1
                else:
                    left+=1
        return result              
```
##C++(118ms)
```cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>>re;
        int l=nums.size();
        int left,right,sum;
        for(int i=0;i<l-2;i++)
        {
            if(i>0&&nums[i]==nums[i-1])continue;
            left=i+1;
            right=l-1;
            if(nums[i]>0&&nums[right]<0)break;
            while(left<right&&nums[left]+nums[i]<=0)
            {
                sum=nums[i]+nums[left]+nums[right];
                if(sum==0)
                {
                    vector<int>temp;
                    temp.push_back(nums[i]);
                    temp.push_back(nums[left]);
                    temp.push_back(nums[right]);
                    re.push_back(temp);
                    left++;
                    right--;
                    while(nums[left]==nums[left-1]&&left<right)left++;
                    while(nums[right]==nums[right+1]&&left<right)right--;
                }
                else if(sum>0)right--;
                else left++;
            }
        }
        return re;
    }
};
```
