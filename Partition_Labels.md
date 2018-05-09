## 题目描述
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
```
Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```
## 解题思路
本来打算是要记录每个字母第一次出现和最后一次出现的位置，然后根据求交并集来求。可是在写代码的过程中发现，这种想法看似简单，实际上实现起来比较难。尤其是求交并集与记录下标真的挺难的。
在Discuss中发现这样一种思路，感觉实现起来确实简单很多。先记录每个字母出现的次数，再遍历一遍数组，设置一个临时的set，用来检测当前的字符串已经是这种元素全部在这部分里。元素全部出现的时候，删除该元素，否则插入。
## C++(10ms)
```cpp
class Solution {
public:
    vector<int> partitionLabels(string S) {
        int dic[26]={0};
        for(int i=0;i<S.size();i++)
            dic[S[i]-'a']++;
        vector<int>re;
        unordered_set<char>strs;
        int index=0;
        for(int i=0;i<S.size();i++)
        {
            if(--dic[S[i]-'a']==0)
            {
                strs.erase(S[i]);
                if(strs.empty())
                {
                    re.push_back(i+1-index);
                    index=i+1;
                }
            }
            else
                strs.insert(S[i]);
        }
        return re;
    }
};
```
