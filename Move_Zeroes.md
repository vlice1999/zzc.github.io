# Description

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```
# Solution
I used a loop to search zeros in this array. If I found zero, I will delete it. I used another loop to add zeros at the end of this array.
# C++(12ms)
```cpp
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int tem = 0;
        int len = nums.size();
        auto it = nums.begin();
        while(it!=nums.end()){
            if(*it == 0)
            {nums.erase(it);tem++;}
            else
                it ++;
        }
        while(tem --)
            nums.push_back(0);
    }
};
```
