## 题目描述
```
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:
Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
 
Example:
Input: "cbbd"

Output: "bb"
```
找到一串字符串中的最长回文字符串
## 题目分析
第一种思路是没到一个字符就检查它的最长回文字符串，这种遍历的速率是python无法接受的，然后看了好久才把Manacher算法看懂。
简单的讲，核心部分就是在一个已知的最后一个回文字符串中，关于中心对称的两个下标处的最长回文字符长度相同。
知道这个有什么用哪？就是缩短回文字符串的搜索时间，只有当目前已知遍历的最后一个回文字符串长度不够时，才去检查是否满足回文字符串的条件。
当然这种方法只适用于长度为奇数的字符串，所以需要插入字符使所有字符串长度都是奇数。
## Python(161ms)
```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s='#'+'#'.join(s)+'#'
        MR=0
        ML=0
        pos=0
        sL=[0]*len(s)
        for i in range(0,len(s)):
            if i<MR:
                sL[i]=min(MR-i,sL[2*pos-i])
            else:
                sL[i]=1
            while i-sL[i]>=0 and i+sL[i]<len(s) and s[i-sL[i]]==s[i+sL[i]]:
                sL[i]+=1
            if i+sL[i]-1>MR:
                MR=i+sL[i]-1
                pos=i
            if ML<sL[i]:
                ML=sL[i]
                longest=s[i-ML+1:i+ML]
        
        i=0
        while longest[i]!=None:
            if longest[i]=='#':
                longest=longest[:i]+longest[i+1:]
            else:
                i+=1
            if i==len(longest):
                return longest
```
## C++(15ms)
```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        string tem="$#";
        for(int i=0;i<s.size();i++){
            tem.push_back(s[i]);
            tem.push_back('#');
        }
        vector<int> len;
        int max_len=0,pos=0,max_right=0,max_id=0;
        for(int i=0;i<tem.size();i++)
            len.push_back(0);
        for(int i=0;i<tem.size();++i){
            if(i<max_right)
               len[i]=len[2*pos-i]>max_right-i?max_right-i:len[2*pos-i];
            else
               len[i]=1;
            while(i-len[i]>=0 && i+len[i]<tem.size()&&tem[i-len[i]]==tem[i+len[i]])
            {
                    len[i]++;
            }
            if(len[i]+i-1>max_right){max_right=len[i]+i-1;pos=i;}
            if(max_len<len[i])
            {
                max_len=len[i];
                max_id=i;
            } 
        }
        string longest_str(tem.substr(max_id-max_len+1,2*max_len-1));
        int i=0;
        while(longest_str[i]){
            if(longest_str[i]!='#'&&longest_str[i]!='$')i++;
            else
            {
                string s1(longest_str.substr(0,i));
                string s2(longest_str.substr(i+1));
                longest_str=s1+s2;
            }
        }
        return longest_str;
    }
};
```
## 总结体会
我就知道我不应该在关灯之前debug，因为总是在关灯之后我才能抓到虫子。
今天用C++做时死活不对，刚刚又查了一遍substr函数脑子才拐个弯来，substr函数的第二个参数是字符串长度，不是下标！！！！！
花有零落日，人有犯二时。或许，我只是比别人二的明显了一点点而已(*/ω＼*)
