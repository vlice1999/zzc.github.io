# Description
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Example 1:
```
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
```
Example 2:
```
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
```
Example 3:
```
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
```
Example 4:
```
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
```
# Solution
My solution is easy to understand. First, I record the length of string S and string T. Then, if I get a `#` when I find every letter in strings, I will delete it.
# C++(0ms)
```cpp
class Solution {
public:
    bool backspaceCompare(string S, string T) {
        int lenS = S.size();
        int lenT = T.size();
        int i = 0;
        while(i < lenS){
            if(S[i] == '#')
            {
                if(i == 0)
                {S.erase(i, 1);lenS--;i --;}
                else{
                    S.erase(i-1, 2);lenS-=2;i -= 2;
                }
            }
            i ++;
        }
        i = 0;
        while(i < lenT){
            if(T[i] == '#')
            {
                if(i == 0)
                {T.erase(i, 1);lenT--;i --;}
                else{
                    T.erase(i-1, 2);lenT-=2;i -= 2;
                }
            }
            i ++;
        }
        return T == S;
    }
};
```
