# Description
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
```
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
```
# Solution
I used map container to store every number's index and then give the array a new number. Then, used string vector to store the result.
# Code(12ms)
```cpp
class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& nums) {
        map<int, int> indexs;
        vector<string> re;
        for(int i = 0;i < nums.size();i ++)
            indexs[nums[i]] = i;
        auto it = indexs.begin();
        int tem = nums.size();
        while(it != indexs.end()){
            re.push_back("0");
            nums[it->second] = tem--;
            it ++;
        }
        for(int i = 0;i < nums.size();i ++){
            if(nums[i] == 1)
                re[i] = "Gold Medal";
            else if(nums[i] == 2)
                re[i] = "Silver Medal";
            else if(nums[i] == 3)
                re[i] = "Bronze Medal";
            else
                re[i] = to_string(nums[i]);
        }
        return re;
    }
};
```
