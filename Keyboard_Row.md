# Description
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
# Solution
I used a map container to store every line's letters. And if I detect that the words all letters' numbers is same to the first letter's number, it's valid.
# C++(0ms)
```cpp
class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        int flag = 0;
        string str1,str2,str3;
        str1 = "qwertyuiopQWERTYUIOP";
        str2 = "ASDFGHJKLasdfghjkl";
        str3 = "zxcvbnmZXCVBNM";
        map<char,int> dict;
        for(int i = 0;i < str1.size();i ++){
            dict[str1[i]] = 1;
        }
        for(int i = 0;i < str2.size();i ++){
            dict[str2[i]] = 2;
        }
        for(int i = 0;i < str3.size();i ++){
            dict[str3[i]] = 3;
        }

        vector<string> re;
        for(int i = 0;i < words.size();i ++){
            flag = dict[words[i][0]];
            for(int j = 1;j < words[i].size();j ++)
            {
                if(dict[words[i][j]] != flag)
                {
                    flag = dict[words[i][j]];
                    break;
                }
            }
            if(flag == dict[words[i][0]])
                re.push_back(words[i]);
        }
        return re;
    }
};
```
