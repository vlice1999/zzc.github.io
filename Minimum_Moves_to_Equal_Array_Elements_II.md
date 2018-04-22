## 题目描述
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
You may assume the array's length is at most 10,000.
## 题目分析
这个题，应该是Math类型中的中等题吧。。。改变数字得到一个相同的数，找到中位数，得到每个数与中位数差的绝对值的和就可以了。
## C++(18ms)
```cpp
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int length=nums.size();
        int pos=length/2,re=0;
        for(int i=0;i<length;i++)
            re+=abs(nums[i]-nums[pos]);
        return re;
    }
};
```
