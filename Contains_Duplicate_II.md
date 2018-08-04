# Description
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
```
Input: nums = [1,2,3,1], k = 3
Output: true
```
Example 2:
```
Input: nums = [1,0,1,1], k = 1
Output: true
```
Example 3:
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```
# Solution
Use a map container to store every letter's last position.
# C++(24ms)
```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int,int>dict;
        for(int i=0;i<nums.size();i++)
        {
            if(dict[nums[i]]==0)
                dict[nums[i]] = i+1;
            else
            {
                if(i+1 - dict[nums[i]]<=k)
                    return true;
                dict[nums[i]] = i+1;
            }
        }
        return false;
    }
};
```
