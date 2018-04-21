## 题目描述
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.
```
Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
```
Example 1:
```
Input: "owoztneoer"

Output: "012"
Example 2:
```
Input: "fviefuro"

Output: "45"
```
这个题幸好幸好，对于输入有要求，要不然就凉凉了。
## 题目分析
直接在这里practice.
``‵
0 zero
1 one
2 two
3 three
4 four
5 five
6 six
7 seven
8 eight
9 nine
```

```
1 z 0
1 w 2
1 u 4
1 x 6
1 g 8
n_i-nums[6]-nums[5]-nums[8] 9
n_f-nums[4] 5
n_o-nums[1]-nums[2]-nums[4] 1
n_r-nums[0]-nums[4] 3
n_s-nums[6] 7
```
## C++(33ms)
```cpp
class Solution {
public:
    string originalDigits(string s) {
        int nums[10]={0};
        int n_f=0,n_r=0,n_o=0,n_s=0,n_i=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='z')nums[0]++;
            if(s[i]=='w')nums[2]++;
            if(s[i]=='u')nums[4]++;
            if(s[i]=='x')nums[6]++;
            if(s[i]=='g')nums[8]++;
            if(s[i]=='i')n_i++;
            if(s[i]=='f')n_f++;
            if(s[i]=='o')n_o++;
            if(s[i]=='r')n_r++;
            if(s[i]=='s')n_s++;
        }
        nums[5]=n_f-nums[4];
        nums[1]=n_o-nums[1]-nums[2]-nums[4]-nums[0];
        nums[3]=n_r-nums[0]-nums[4];
        nums[7]=n_s-nums[6];
        nums[9]=n_i-nums[6]-nums[5]-nums[8];
        string re;
        for(int i=0;i<10;i++)
            for(int j=0;j<nums[i];j++)
                re+=std::to_string(i);
        return re;
    }
};
```
