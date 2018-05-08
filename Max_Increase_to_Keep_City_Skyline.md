## 题目描述
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?
```
Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

```
## 解题思路
其实还是蛮简单的一个题，就是字比较多。先遍历一遍数组，找到自上向下的每列的最大值，还有自左向右每行的最大值就可以。再遍历一遍后得差求和。
## C++(10ms)
```cpp
class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int row=grid.size();
        int col=grid[0].size();
        int t_b[col]={0},l_r[row]={0};
        int re=0;
        for(int i=0;i<row;i++)
            for(int j=0;j<col;j++)
            {
                t_b[j]=t_b[j]>grid[i][j]?t_b[j]:grid[i][j];
                l_r[i]=l_r[i]>grid[i][j]?l_r[i]:grid[i][j];
            }
        for(int i=0;i<row;i++)
            for(int j=0;j<col;j++)
                re+=min(t_b[j],l_r[i])-grid[i][j];
        return re;
    }
};
```
