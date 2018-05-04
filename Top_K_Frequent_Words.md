## 题目描述
Given a non-empty list of words, return the k most frequent elements.
```
Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
```
Example 1:
```
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
```
Example 2:
```
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
```
## 题目分析
这个题按出现次数排序很好弄，用map然后按照<string,int>存放，再按值排序。然而，卡在了相同次数的字符串怎么排序上，一开始以为是要按长度排序，最后发现，原来直接用string的比大小就可以了（可怜了我的AC率）。
## C++(16ms)
```cpp
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string,int>Map;
        for(int i=0;i<words.size();i++)
        {
            string s;
            s=words[i];
            Map[s]++;
        }
        vector<pair<string,int>>vtMap;
        for(auto it=Map.begin();it!=Map.end();it++)
        vtMap.push_back(make_pair(it->first,it->second));
        sort(vtMap.begin(),vtMap.end(),[](const pair<string,int> &x,const pair<string,int> & y)->int{return x.second>y.second;});
        vector<string>re;
        int len=0;
        for(auto it=vtMap.begin();it != vtMap.end();it++,len++)
        {
            re.push_back(it->first);
            if(len>0)
            {
                auto pre=it;
                pre--;
                int len_=len;
                while(it->second==pre->second)
                {
                    pre--;
                    len_--;
                }
                sort(re.begin()+len_,re.end(),[](const string &x,const string &y)->bool{return x<y;});
              //sort(re.begin()+len_,re.end(),less<string>());这样写效果相同。
            }
        }
        vector<string> R(re.begin(),re.begin()+k);
        return R;
    }
};
```
## 感悟
完美，哈哈。get一种新的sort排序写法，以后多试试，嘿嘿
