# Description
Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. Your expression should NOT contain redundant parenthesis.

Example:
```
Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
since they don't influence the operation priority. So you should return "1000/(100/10/2)". 

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
```
# Solution
It looks like a strange problem becuase if the number of numbers is more than two, the result will be constant. And, it's really so strange. 
# C++(0ms)
```cpp
class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        string re = "";
        if(nums.size() == 0)
            return re;
        if(nums.size() == 1)
            return to_string(nums[0]);
        if(nums.size() == 2)
        {
            re += to_string(nums[0]);
            re += '/';
            re += to_string(nums[1]);
        }
        else{
            re += to_string(nums[0]);
            re += "/(";
            int i = 1;
            for(;i < nums.size()-1;i ++)
            {
                re += to_string(nums[i]);
                re += '/';
            }
            re += to_string(nums[i]);
            re += ')';
        }
        return re;
    }
};
```
