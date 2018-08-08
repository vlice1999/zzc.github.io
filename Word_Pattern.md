# Description
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
```
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
```
Example 2:
```
Input:pattern = "abba", str = "dog cat cat fish"
Output: false
```
Example 3:
```
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
```
Example 4:
```
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
```
# Solution
I think the map container can do anything hhhhh. And this problem I use a new way to split the string str. Like this:
```cpp
istringstream sin(s); sin>>t; 
```
# C++(0ms)
```cpp
class Solution {
public:
    bool wordPattern(string pattern, string str) {
        string tem1="", tem2="";
        string str_tem;
        map<char, int> dic1;
        map<string, int> dic2;
        int index = 0;
        for(int i = 0; i < pattern.size(); i ++)
        {
            if(!dic1[pattern[i]])
                dic1[pattern[i]] = ++ index;
            tem1 += to_string(dic1[pattern[i]]);
        }
        
        index = 0;
        for(istringstream is(str); is >> str_tem;){
            if(!dic2[str_tem])
                dic2[str_tem] = ++index;
            tem2 += to_string(dic2[str_tem]);
        }
        
        return tem1 == tem2;
    }
};
```
