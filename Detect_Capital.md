# Description
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
# Solution
I used two pointers to judge if the string contains capitals or not capitals. If the first letter is capitals, ignore it. And if the string contains both capital and not capital, return false.
# C++(4ms)
```cpp
class Solution {
public:
    bool detectCapitalUse(string word) {
        if(word.size() == 1)
            return true;
        bool flag1 = 0, flag2 = 0;
        if('a' <= word[0])
            flag1 = 1;
        for(int i = 1;i < word.size();i ++)
        {
            if(word[i] <= 'Z')
                flag2 = 1;
            if('a'<= word[i])
                flag1 = 1;
            if(flag1 == flag2)
                return false;
        }
        return !(flag1 && flag2);
    }
};
```
