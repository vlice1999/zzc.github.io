# Permutations_I
## 题目描述
```
 Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```
给一组不同的数字，返回他们所有可能的组合
## 解题思路
回溯算法，遍历的时候弹出当前元素，成叉形扩散。
## C++(15ms)
```cpp
class Solution {
public:
    void dfs(vector<vector<int>>&res,vector<int> nums,vector<int> temp,int l)
    {
        if(temp.size()==l)res.push_back(temp);
        for(int i=0;i<nums.size();i++){
            int r=nums[i];
            temp.push_back(r);
            nums.erase(nums.begin()+i);
            dfs(res,nums,temp,l);
            temp.pop_back();
            nums.insert(nums.begin()+i,r);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>>res;
        vector<int>temp;
        int l=nums.size();
        dfs(res,nums,temp,l);
        return res;
    }
};
```
## Python(100ms)
```python
class Solution(object):
    def dfc(self,nums,temp,l):
        if len(temp)==l:
            Solution.re.append(temp)
        else:
            for i in range(len(nums)):
                strs=nums[:i]+nums[i+1:]
                self.dfc(strs,temp+[nums[i]],l)
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.re=[]
        self.dfc(nums,[],len(nums))
        return Solution.re
```
# Permutaitoins_II
## 题目描述
和上个题类似，不过是数组中有重复元素了
## 解题思路
万能的回溯，哈哈～～～
## C++(26ms)
```
class Solution {
public:
    void dfs(vector<vector<int>>&res,vector<int> nums,vector<int> temp,int l)
    {
        if(temp.size()==l)res.push_back(temp);
        for(int i=0;i<nums.size();i++){
            if(i!=0&&nums[i]==nums[i-1])continue;
            int r=nums[i];
            temp.push_back(r);
            nums.erase(nums.begin()+i);
            dfs(res,nums,temp,l);
            temp.pop_back();
            nums.insert(nums.begin()+i,r);
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>>res;
        vector<int>temp;
        int l=nums.size();
        sort(nums.begin(),nums.end());
        dfs(res,nums,temp,l);
        return res;
    }
};
```
## Python(203ms)
```python
class Solution(object):
    def dfs(self,nums,temp,l):
        if len(temp)==l:
            Solution.re.append(temp)
        else:
            for i in range(len(nums)):
                if nums[i]==nums[i-1] and i!=0:
                    continue
                strs=nums[:i]+nums[i+1:]
                self.dfs(strs,temp+[nums[i]],l)
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.re=[]
        nums.sort()
        self.dfs(nums,[],len(nums))
        return Solution.re
```
## Python(121ms)
```python
class Solution(object):
    def dfc(self,nums,temp,l):
        if len(temp)==l:
            Solution.re.append(temp)
        else:
            for i in range(len(nums)):
                tem=nums[i]
                if nums[i]==nums[i-1] and i!=0 or nums[i]=="0":
                    continue
                nums[i]="0"
                self.dfc(nums,temp+[tem],l)
                nums[i]=tem
                
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.re=[]
        nums.sort()
        self.dfc(nums,[],len(nums))
        return Solution.re
(充分利用python的优势)
```

# 总结体会
再看见必须遍历所有组合的题，直接回溯，哈哈。
