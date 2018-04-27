## 题目描述
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
```
Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99]) 
```
## 题目分析
其实，这个题，真的是毫无存在感。要返回找到数字中不出现重复数字的数：n=0,re=1;
n=1,re=10;n=2,re=1+10*9;n=3,re=1+10*9+10*9*8;...n=N(N>2),re=re+re*[10-n+1].
## C++(2ms)
```cpp
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if(n==0)return 1;
        if(n==1)return 10;
        int re=10,tem=9;
        for(int i=2;i<=n;i++)
        {
            tem*=(9-i+2);
            re+=tem;
        }
        return re;
    }
};
```
