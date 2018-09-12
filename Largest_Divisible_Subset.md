# Description
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
```
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
```
Example 2:
```
Input: [1,2,4,8]
Output: [1,2,4,8]
```
# C++(16ms)
```cpp
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        vector<int> re;
        if(nums.size() == 0)
            return re;
        
        sort(nums.begin(), nums.end());
        int max_len = 0, max_index = -1;
        int dp[nums.size()], index[nums.size()];
        for(int i = 0;i < nums.size();i ++){
            dp[i] = 1;
            index[i] = -1;
        }
        
        for(int i = 0;i < nums.size();i ++){
            for(int j = 0;j < i;j ++){
                if(nums[i]%nums[j] == 0 && dp[i] < dp[j]+1){
                    dp[i] = dp[j] + 1;
                    index[i] = j;
                }
            }
            if(dp[i] > max_len){
                max_len = dp[i];
                max_index = i;
            }
        }

        while(1){
            if(max_index != -1)
            {
                re.push_back(nums[max_index]);
                max_index = index[max_index];
            }
            else
                break;
        }
        reverse(re.begin(), re.end());
        return re;
    }
};
```
