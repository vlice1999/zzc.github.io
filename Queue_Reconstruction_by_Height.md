## 题目描述
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue. 
```
Example 
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```
## 解题思路
相当神奇的一个排序题。题目大意是第一个数代表个头，第二个数代表前面比他高（包括与他相等）的人的个数。给出来的是乱的，排好序后返回。

可以先按个头从大到小排序，个头相等的按前面的人数从小到大排序。这时候只需要按照people[i].second向re中插入元素就好了。因为此时re[people[i].second]前面就是比他高（包括与他相等）的人，而且插入这个人后，对于后面比他高的人的second不产生任何影响。

以原题所给例子为例
```
先排序：
[[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
向re中依次插入元素：
re=[[7,0]]
re=[[7,0],[7,1]]
re=[[7,0],[6,1],[7,1]]
re=[[5,0],[7,0],[6,1],[7,1]]
re=[[5,0],[7,0],[5,2],[6,1],[7,1]]
re=[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
```
## C++(36ms)
```cpp
class Solution {
public:
    static bool comp(const pair<int,int> &a,const pair<int,int>&b)
    {
        return(a.first>b.first||(a.first==b.first && a.second < b.second));
    }
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        sort(people.begin(),people.end(),comp);
        vector<pair<int,int>>re;
        for(int i=0;i<people.size();i++)
            re.insert(re.begin()+people[i].second,people[i]);
        return re;
    }
};
```
