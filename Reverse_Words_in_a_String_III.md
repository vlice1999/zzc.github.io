# Description
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


Example 1:
```
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```
# C++(16ms)
```cpp
class Solution {
public:
    string reverseWords(string s) {
        string re = "";
        string temp;
        stringstream input(s);
        while(input >> temp){
            reverse(temp.begin(), temp.end());
            re += temp;
            re += ' ';
        }
        re.pop_back();
        return re;
    }
};
```
