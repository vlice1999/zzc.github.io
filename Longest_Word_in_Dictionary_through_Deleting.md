## 题目描述
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
```
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
```
Example 2:
```
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
```
## 题目分析
注意比较的条件，一是符合“删除”的要求，然后返回最长的那个，最长的有多个返回最小的那个
## C++(96ms)
```cpp
class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        sort(d.begin(),d.end(),[](const string &x,const string &y)->bool{return x.size()==y.size()?x<y:x.size()>y.size();});
        for(int i=0;i<d.size();i++)
            if(check(s,d[i]))
                return d[i];
        return "";
    }
    bool check(string s,string str)
    {
        for(int i=0;i<str.size();)
        {
            for(int j=0;j<s.size();)
            {
                if(str[i]==s[j])
                {
                    i++;
                    j++;
                }
                else
                    j++;
            }
            if(i!=str.size())return 0;
        }
        return 1;
    }
};
```
