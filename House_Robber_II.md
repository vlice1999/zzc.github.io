# Description
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
```
Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```
# Solution
Now, all houses at this place are arranged in a circle. And the only difference is that the first house is the neighbor of the last one. So, I only need to make two arrays, and earse the first neighbor or earse the last neighbor. Then return the maximum between them.
# C++(0ms)
```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        int len = nums.size(), tem1 = 1;
        vector<int> index;
        for(int i=1;i<len;i++)
            index.push_back(nums[i]);
        nums.pop_back();
        if(len == 0)
            return 0;
        if(len == 1)
            return nums[0];
        if(len == 2)
            return max(nums[0],nums[1]);
        return max(help(nums),help(index));
    }
    int help(vector<int>& robs){
        int len = robs.size();
        if(len == 2)
            return max(robs[0],robs[1]);
        robs[1] = max(robs[0],robs[1]);
        for(int i = 2; i<len ; i ++)
            robs[i] = max(robs[i]+robs[i-2],robs[i-1]);
        return robs[len-1];
    }
};
```
