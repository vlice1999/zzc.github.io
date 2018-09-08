# Description
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:
```
Input: [3,2,3]
Output: [3]
```
Example 2:
```
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
```
# Solution
I solve this problem by using a easy method. First, sort this array. Then, use a number to record the number of every number and use another number to record the current number. If the current numeber is different with the recorded number and the number of the recorded number is bigger than n/3, that's the number I wanner.
# C++(12ms)
```cpp
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> re;
        if(nums.size() == 0)
            return re;
        sort(nums.begin(), nums.end());
        int tem = nums[0];
        int num = 0;
        int len = nums.size();
     
        for(int i = 0;i < len;i ++)
        {
            if(nums[i] != tem){
                if(num <= len/3){
                    tem = nums[i];
                    num = 1;
                }
                else{
                    re.push_back(tem);
                    tem = nums[i];
                    num = 1;
                }
            }
            else{
                num ++;
            }
        }
        if(num > len/3)
            re.push_back(tem);
        return re;
    }
};
```
