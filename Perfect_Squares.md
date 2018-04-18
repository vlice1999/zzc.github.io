## 题目描述
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n. 
For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9. 
`` ``
给一个正整数n，找到平方数的和为n的整数个数。
## 题目分析
从小到大依次记录每个值所对应的平方数为n的整数个数。即nums[i]=nums[i-j*j](i>=j*j)
## C++(110ms)
```
class Solution {
public:
    int numSquares(int n) {
        int nums[n+1];
        for(int i=0;i<=n;i++)nums[i]=i;
        for(int i=2;i<=n;i++)
        {
            for(int j=1;j*j<=i;j++)
                nums[i]=min(nums[i],nums[i-j*j]+1);
        }
        return nums[n];
    }
};
```
