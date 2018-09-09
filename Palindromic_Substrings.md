# Description
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
```
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```
Example 2:
```
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```
# Solution
I used an easy method to solve this problem, but it takes a long time. I made two function, one of which is to judge if it is a palindromic string and another is to help get all combinations.
# C++(616ms)
```cpp
class Solution {
private:
    int re = 0;
public:
    int countSubstrings(string s) {
        help(s);
        return re;
    }
    bool isPalindromic(string s){
        string s_;
        s_ = s;
        reverse(s.begin(), s.end());
        //cout << s_ << endl;
        if(s_ == s)
            return 1;
        return 0;
    }
    void help(string s){
        int len = s.size();
        for(int i = 1;i <= len;i ++){
            re += isPalindromic(s.substr(0, i));
            //cout << s <<" "<< i<< endl;
        }
        if(len > 0)
            help(s.substr(1, len));
    }
};
```
