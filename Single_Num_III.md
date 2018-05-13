## 题目描述
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:
```
Input:  [1,2,1,3,2,5]
Output: [3,5]
```
## 解题思路
直接用map做了，大神们的位运算没有看懂，因为对于二进制这一块真的不大了解。
## C++(19ms)
```cpp
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        map<int,int>Map;
        for(int i=0;i<nums.size();i++)
            Map[nums[i]]++;
        vector<int>re;
        for(auto i=Map.begin();i!=Map.end();i++)
            if(i->second==1)
                re.push_back(i->first);
        return re;
    }
};
```
