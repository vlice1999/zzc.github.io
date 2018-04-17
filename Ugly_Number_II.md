## 题目描述
```
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690. 
```
## 题目分析
丑数的定义就是质因子只有2，3，5的数。那么要找到第n个质因子，就需要让它之前的数都与2，3，5相乘，直到找到最小的与2，3，5相乘比目前丑数大的数。
用t2,t3,t5分别记录当前数组中与最末尾的丑数最接近的数(此处的最接近是指：t2最接近末尾丑数x则nums[t2]*2最靠近x)。在比较时仅需要比较最靠近末尾丑数的三个值即可。
## C++(363ms)
```cpp
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> uglyNum(n);
        int num[3]={0,0,0};
        if(n<7)
            return n;
        uglyNum={1,2,3,4,5,6};
        int tem=0;
        int len=5;
        for(int i=5;i<n-1;i++)
        {
            for(int j=1;j<i;j++)
                if(uglyNum[j]*2>uglyNum[i])
                {
                    num[0]=uglyNum[j]*2;
                    break;
                }
            for(int j=1;j<i;j++)
                if(uglyNum[j]*3>uglyNum[i])
                {
                    num[1]=uglyNum[j]*3;
                    break;
                }
            for(int j=1;j<i;j++)
                if(uglyNum[j]*5>uglyNum[i])
                {
                    num[2]=uglyNum[j]*5;
                    break;
                }
            uglyNum[i+1]=min(num[0],min(num[1],num[2]));
        }
        return uglyNum[n-1];
    }
};
```
## C++(7ms)
```cpp
class Solution {
public:
    int nthUglyNumber(int n) {
        int num[n];
        int t2=0,t3=0,t5=0;
        if(n<7)
            return n;
        num[0]=1;
        for(int i=1;i<n;i++)
        {
            num[i]=min(num[t2]*2,min(num[t3]*3,num[t5]*5));
            if(num[i]==num[t2]*2)t2++;
            if(num[i]==num[t3]*3)t3++;
            if(num[i]==num[t5]*5)t5++;
        }
        return num[n-1];
    }
};
```
