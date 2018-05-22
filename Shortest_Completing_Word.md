## 题目描述
Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate 
Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word. 
It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array. 
The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does. 
```
Example 1:
Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.

Example 2:
Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: There are 3 smallest length words that contains the letters "s".
We return the one that occurred first.

Note:
licensePlate will be a string with length in range [1, 7].
licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
words will have a length in the range [10, 1000].
Every words[i] will consist of lowercase letters, and have length in range [1, 15].
```
## 解题思路
这个题思路还是挺简单的，就是用一个数组记录下licensePlate中各字母出现的次数，注意一下要把大写字母换成小写字母，然后check一下words中单词是否符合条件。

check的方法有技巧，这里map其实赶不上int[]方便，因为只需要记录数量就好了，而且int[]类型更方便同时搜索两个字符串各字母出现的次数。

符合条件的，判断长度是否小于当前最小长度就好了。
## C++(15ms)
```cpp
class Solution {
public:
    bool check(string s, int dic[])
    {
        int dic_[26]={0};
        for(int i=0;i<s.size();i++)
            dic_[s[i]-'a']++;
        for(int i=0;i<26;i++)
            if(dic_[i]<dic[i])
                return false;
        return true;
    }
    string shortestCompletingWord(string licensePlate, vector<string>& words) {
        string a,s;
        transform(licensePlate.begin(),licensePlate.end(),a.begin(),::tolower);
        s=a.c_str();
        int dic[26]={0};
        for(int i=0;i<s.size();i++)
            if('a'<=s[i]&&s[i]<='z')
                dic[s[i]-'a']++;
        string re;
        int minLength=16;
        for(int i=0;i<words.size();i++)
        {
            if(check(words[i],dic))
                if(words[i].size()<minLength)
                {
                    re=words[i];
                    minLength=words[i].size();
                }
        }
        return re;
    }
};
```
