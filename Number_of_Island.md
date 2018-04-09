## 题目描述
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
```
Example 1:
11110
11010
11000
00000
Answer: 1
Example 2:
11000
11000
00100
00011
Answer: 3
```
## 问题分析
我首先想到的是判断周围是不是有连着的岛屿，没有的话岛屿数量加一。这个想法很好，实现起来却很尴尬。因为上下左右有一个是“1”就不能算是孤立的一个岛，只能从一个“1”走到另一个“1”直到走不动为止。
这个走的方式让我想到了竞赛时XX回家的题，在规定步数内看能不能到家。因为步数规定了，所以不怕回溯超时，来回走就可以。这个题要想回溯，就得让小岛先被水淹了，要不然就会陷入死循环了。
其实被水淹的方式也是多种多样的，关键在于理解。我一开始的思路是“淹”的“1”周围全是“0”的时候，加一。可代码写起来相当费劲（因为需要判断边角的情况），而且我python代码超了递归深度，debug无果。
在网上看见一个比较厉害的“淹”岛的代码，人家一淹淹一片，从头开始一次遍历，遇见“1”就把那一片淹了，然后找下一个岛屿。。。
## Python(131ms)
```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid,i,j):
            if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0])):
                return 
            elif grid[i][j]=='1':
                grid[i][j]='0'
                dfs(grid,i-1,j)
                dfs(grid,i,j-1)
                dfs(grid,i+1,j)
                dfs(grid,i,j+1)
            return 
        
        nums=0
        row=len(grid)
        if row==0:
            return 0
        col=len(grid[0])
        if col==0:
            return 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    nums+=1
                    dfs(grid,i,j)
        return nums
```
## C++(13ms)
```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int num_of_island=0;
        for(int i=0;i<grid.size();i++)
            for(int j=0;j<grid[i].size();j++)
                if(grid[i][j]=='1'){
                    num_of_island++;
                    dfs(grid,i,j);
                }
        return num_of_island;
    }
    void dfs(vector<vector<char>>& grid,int i,int j){
        if((i<0)||(j<0)||(i>=grid.size())||(j>=grid[0].size()))
            return;
        else if(grid[i][j]=='1'){
            grid[i][j]='0';
            dfs(grid,i-1,j);
            dfs(grid,i+1,j);
            dfs(grid,i,j-1);
            dfs(grid,i,j+1);
        }
        return;
    }
};
```
