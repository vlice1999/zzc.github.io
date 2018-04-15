## 题目描述
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students. 
```
Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.

Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Note:

    N is in range [1,200].
    M[i][i] = 1 for all students.
    If M[i][j] = 1, then M[j][i] = 1.

```
## 题目分析
其实静下心来看题，发现这个题也不是很难弄。首先，需要搞清楚的的是，一共只有n个人，不是n*n个，一开始还在想会不会有n*m这种情况，真的是傻到家了。
确定有n个人之后，就判断每个人是否有朋友圈，或者已经有了一个朋友圈（根据题意，每个人至多有一个朋友圈），回溯的时候就把他排除就可以了。
因为M[i][j]=1，表示i和j互为朋友，M[j][k]=1，表示i和k为间接朋友，所以知道M[i][j]是1后，就去回溯M[j][0~n]，标记已经有朋友圈的人，避免再次回溯时重复计数。
## C++(22ms)
```cpp
class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int re=0;
        vector<int> tem(M.size(),0);
        for(int i=0;i<M.size();i++)
        {
            if(tem[i]==0)
            {
                re++;
                dfs(tem,M,i);
            }
        }
        return re;
    }
    void dfs(vector<int> &tem,vector<vector<int>>& M,int line)
    {
        for(int i=0;i<M[line].size();i++)
        {
            if(tem[i]==0 && M[line][i]==1){
                tem[i]=1;
                dfs(tem,M,i);
            }
        }
    }
};
```
## Python(61ms)
```python
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        tem=len(M)*[0]
        cout=0
        for i in range(len(M)):
            if tem[i]==0:
                cout+=1
                self.dfs(M,tem,i)
        return cout
    def dfs(self,M,tem,line):
        for i in range(len(M)):
            if M[line][i]==1 and tem[i]==0:
                tem[i]=1
                self.dfs(M,tem,i)
```
