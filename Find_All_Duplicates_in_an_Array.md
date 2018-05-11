## 题目描述
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
```
Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```
## 解题思路
①用map记录每个数字出现的次数，然后再遍历map找到出现两次的元素。这种方法很慢，而且是不符合题目要求的。
②题目中有一个限制条件是1<=a[i]<=n，也就是说里面所有的数字都有对应下标。而且除了一次就是两次。可以让每个数字对应下标的数字×(-1)，这样出现一次的数字对应下标的数字就是负数，出现两次的数字对应下标出现的数字就是正数。
## C++(207ms)
```cpp
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        map<int,int>Map;
        for(int i=0;i<nums.size();i++)
            Map[nums[i]]++;
        vector<int>re;
        for(auto i=Map.begin();i!=Map.end();i++)
        {
            if(i->second==1)
                continue;
            re.push_back(i->first);
        }
        return re;
    }
};
```
##C++(127ms)
```cpp
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int>re;
        for(int i=0;i<nums.size();i++){
            nums[abs(nums[i])-1]=-nums[abs(nums[i])-1];
            if(nums[abs(nums[i])-1]>0)
                re.push_back(abs(nums[i]));
        }
        return re;
    }
};
```
