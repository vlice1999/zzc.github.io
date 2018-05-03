## 题目描述
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
```
Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
```
在一段数组中，如果连续子串中有0和1的数量相同，返回子串的长度
## 题目分析
首先，这个题，肯定不是用for循环来做，所以题目就感觉比较难了。那么，就要想法记录每个下标出0和1累计出现的次数，如果是分开处理，太麻烦。就让0全等于-1，这样求和之后就大致知道0和1间的数量关系。假如目前sum=3，那么1比0多三个，去找上一个sum=3的位置，他们之间的0和1的数量就是相等的。
## 解题思路
变0为-1，sum记录当前0和1的数量关系。去找上一个sum的值，有的话，就是maxLen=max(maxLen,i-Map[sum])，没有的话，Map[sum]=i，插入新数据。
## C++(149ms)
```cpp
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        if(nums.size()==0)return 0;
        map<int,int>Map;
        map<int,int>::iterator it;
        it=Map.begin();
        Map[0]=-1;
        int maxLen=0,sum=0;
        for(int i=0;i<nums.size();i++)
        {
            sum+=(nums[i]==0)?-1:1;
            it=Map.find(sum);
            if(it!=Map.end())
                maxLen=max(maxLen,i-it->second);
            else
                Map[sum]=i;
        }
        return maxLen;
    }
};
```
这么完美的代码竟然只超过了50%的人，这不科学。。。
