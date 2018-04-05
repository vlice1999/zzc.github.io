## 题目描述
```
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks. 
The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right. 
If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks. 
You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks. 
Example:
Input: 
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
Output: 2
Note:
The width sum of bricks in different rows are the same and won't exceed INT_MAX.
The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000. 
```
## 题目分析
这个题的的意思就是得到最小的穿墙数目，换句话说就是得到墙相等的数目（不包括最后一个墙）。看到这种题，如果用土办法就是申请一个与墙总长相等的数组，记录“间隙”的个数，当遇到总长为2^31这种情况只能呵呵了。所以，关键时刻还是要看map函数的。
## 解题思路
申请一个map，Key为墙长，Value为这种墙长的个数。遍历墙，记录，最后求出Value的最大值。
## C++(41ms)
```cpp
class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        map<int,int> re;
        map<int ,int>::iterator it;
        int sum,max=0;
        for(int i=0;i<wall.size();i++)
        {
            sum=0;
            for(int j=0;j<wall[i].size()-1;j++)
            {
                sum+=wall[i][j];
                ++re[sum];
            }
        }
        for(it=re.begin();it!=re.end();it++)
            max=it->second>max?it->second:max;
        return wall.size()-max;
    }
};
```
