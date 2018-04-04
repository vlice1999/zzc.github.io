## 题目描述
A message containing letters from A-Z is being encoded to numbers using the following mapping: 
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it. 
For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12). 
The number of ways decoding "12" is 2. 
## 题目分析
看到这个题，直接递归了，然后没悬念的超时了。借鉴了别人的代码，采用动态规划的方式来解决。
## 解题思路
申请一个长度比字符串长度大一的空数组，头两个元素赋值1，用来记录到达当前遍历字符的组合数。
字符串两个为一组，如果这一组的值在[10,26]之间并且不是10或20，那么re[i]=re[i-1]+re[i-2]
为10或20，re[i]=re[i-2]
头一个元素为[3,9],re[i]=re[i-1]
其余情况，返回0
## python(47ms)
```python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """         
        if s=="" or s[0]=="0":
            return 0
        re=[0]*(len(s)+1)
        re[0],re[1]=1,1
        for i in range(2,len(s)+1):
            if 10<int(s[i-2:i])<=26 and (s[i-1])!="0":
                re[i]=re[i-1]+re[i-2]
            elif int(s[i-2:i])==10 or int(s[i-2:i])==20:
                re[i]=re[i-2]
            elif s[i-1]!="0":
                re[i]=re[i-1]
            else:
                return 0
        return re[len(s)]
```
## C++(4ms)
```cpp
class Solution {
public:
    int numDecodings(string s) {
        vector<int> result;
        int len=s.length(),temp=0;
        result.push_back(1);
        result.push_back(1);
        if(len==0||s[0]=='0')return 0;
        if(len==1&&s[0]!='0')return 1;
        for(int i=2;i<=len;i++)
        {
            temp=atoi(s.substr(i-2,2).c_str());
            if(10<temp && temp<=26 && temp!=20)
                result.push_back(result[i-2]+result[i-1]);
            else if(temp==10||temp==20)
                result.push_back(result[i-2]);
            else if(s[i-1]!='0')
                result.push_back(result[i-1]);
            else 
                return 0;
        }
        return result[len];
    }
};
```
## 解题感悟
目前看来，用了string后的C++和python的代码差不了几行，而且巨快୧(๑•̀◡•́๑)૭
