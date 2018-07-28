# Description
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
```
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```
# Solution
Firstly, I wanted to cut this matrix, but I fonud it's impossible to solve this problem because I don't have a valid way to cut it. 


I saw a correct way which is to record the largest square's side at every position and the fomular is: deep[i][j] = 1 + min(deep[i-1][j-1],min(deep[i-1][j],deep[i][j-1])). And the thinking map like this:
```
1 1 1 1 ...
1 2 2 2 ...
1 2 3 3 ...
1 2 3 4 ...
. . . .
. . . .
. . . .
```
# C++(12ms)
```c++
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int row = matrix.size();
        if(row == 0)
            return 0;
        int col = matrix[0].size();
        vector<vector<int>> deep(row,vector<int>(col,0));
        int ans = 0;
        for(int i=0;i<row;i++)
            for(int j=0;j<col;j++)
            {
                if(matrix[i][j] == '1')
                    deep[i][j] = (i==0||j==0) ? 1:1+min(deep[i-1][j-1],min(deep[i-1][j],deep[i][j-1]));
                ans = max(ans,deep[i][j]);
            }
        return ans*ans;
    }
};
```
