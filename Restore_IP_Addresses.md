## 题目描述
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

```
Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```
## 题目分析
首先，得明白ip满足的条件,每块ip都小于256。
## 解题思路
只需要设置一个函数检查每块ip是否符合条件，然后主函数中设置三层for循环分割ip即可。但是需要注意的是，题目所给的ip长度可能不对，而且不能有‘010’这种情况。
## C++(4ms)
```cpp
class Solution {
public:
    bool check(string s){
        int num=0;
        for(int i=0;i<s.size();i++)
            num=num*10+(s[i]-'0');
        if(s[0]=='0')
            return s.size()==1;
        return num<256;
    }
    vector<string> restoreIpAddresses(string s) {
        vector<string> re;
        if(s.size()<4 || s.size()>12)
            return re;
        for(int i=1;i<s.size()-2;i++)
            for(int j=i+1;j<s.size()-1;j++)
                for(int k=j+1;k<s.size();k++)
                {
                    string ip1=s.substr(0,i);
                    string ip2=s.substr(i,j-i);
                    string ip3=s.substr(j,k-j);
                    string ip4=s.substr(k);
                    if(ip1.size()<4&&ip2.size()<4&&ip3.size()<4&&ip4.size()<4)
                    {
                    if(check(ip1) && check(ip2) && check(ip3) && check(ip4))
                    {
                        string tem;
                        tem=ip1+'.'+ip2+'.'+ip3+'.'+ip4;
                        re.push_back(tem);
                    }
                    }
                }
        return re;
    }
};
```
