## 题目描述
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
```
Example:
For num = 5 you should return [0,1,1,2,1,2].
```
Follow up:
```
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
```
## 题目分析
先从网上找到了1-100的二进制数表，然后通过前十五个找到了规律。
```
0=0
1=1
2=10
3=11
4=100
5=101
6=110
7=111
8=1000
9=1001
10=1010
11=1011
12=1100
13=1101
14=1110
15=1111
从这这张表中可以看出除了re[0]=0,其余都是re[i]=re[i/2]+i%2.
```
## C++(71ms)
```cpp
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> re(num+1,0);
        if(num==0)return re;
        for(int i=1;i<num+1;i++)
            re[i]=re[i/2]+i%2;
        return re;
    }
};
```
