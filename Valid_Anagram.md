# Description
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```
Example 2:
```
Input: s = "rat", t = "car"
Output: false
```
# Solution
I have two ways to solve this problem. I can get the numbers of string s and string t's letters, and judge if the every letter's number is same. And I also can sort the two strings and judge if they are same or not.
# C++
```cpp
// Code 1:
class Solution {
public:
    bool isAnagram(string s, string t) {
        int dic[26] = {0};
        if(s.size()!=t.size())
            return false;
        for(int i=0;i<s.size();i++)
            dic[s[i]-'a'] ++;
        for(int i=0;i<t.size();i++)
        {
            dic[t[i]-'a'] --;
            if(dic[t[i]-'a']<0)
                return false;
        }
        return true;
    }
};
// Code 2:
class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }
};
```
