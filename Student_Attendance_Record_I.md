# Description
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
```
Input: "PPALLP"
Output: True
```
Example 2:
```
Input: "PPALLL"
Output: False
```
# Solution
I set two flags to judge the number of A and the number of L, and if A's number is bigger than 1 or more than two continuous 'L', return false.
# C++(0ms)
```cpp
class Solution {
public:
    bool checkRecord(string s) {
        int flag_A = 0;
        int flag_L = 0;
        for(int i = 0;i < s.size();i ++){
            if(s[i] == 'A')
                flag_A ++;
            if(s[i] == 'L')
                flag_L ++;
            else
                flag_L = 0;
            if(flag_A==2||flag_L==3)
                return false;
        }
        return true;
    }
};
```
