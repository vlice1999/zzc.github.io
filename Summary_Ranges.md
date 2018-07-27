# Description
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
```
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
```
Example 2:
```
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
```
# Solution
The thinking is to store the temporary minimum first. 
<bar>
If the current number subtract the minimum is bigger than 1 and the previous number is not the minimum, add string(minimum+"->"+previous number) to result-vector. And if the previous number is the minimum, add string(minimum) to result-vector.
# C++(0ms)
```c++
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> tem_nums;
        if(nums.size()==0)
            return tem_nums;
        int tem = nums[0];
        if(nums.size()==1)
        {
            tem_nums.push_back(to_string(tem));
            return tem_nums;
        }
        string punc = "->";
        for(int i=1;i<nums.size();i++){
            cout << nums[i] <<" "<<nums[i-1]<<endl;
            if(nums[i] - nums[i-1] > 1 || nums[i]-nums[i-1]<0)
            {
                if(nums[i-1] == tem)
                    tem_nums.push_back(to_string(nums[i-1]));
                else
                    tem_nums.push_back(to_string(tem)+punc+to_string(nums[i-1]));
                tem = nums[i];
            }
            if(i == nums.size()-1){
                if(nums[i]-nums[i-1]==1)
                    tem_nums.push_back(to_string(tem)+punc+to_string(nums[i]));
                if(nums[i]-nums[i-1]>1 || nums[i] - nums[i-1]<0)
                    tem_nums.push_back(to_string(nums[i]));
            }
        }
        return tem_nums;
    }
};
```
