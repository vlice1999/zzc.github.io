# Description
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
\\
A region is captured by flipping all 'O's into 'X's in that surrounded region.
\\
Example:
```
X X X X
X O O X
X X O X
X O X X
```
After running your function, the board should be:
```
X X X X
X X X X
X X X X
X O X X
```
# Solution
My thinking is to build a new int "numboard"(int) first, then iterates through "board".If board[i][j] is "X", the numboard[i][j] is "1", otherwise, it is zero.\\
Then use dfs to iterates through the board boundary. If board[i][j] is "O", we begin foreach, and numboard[i][j] is "-1".\\
Last, iterates through the "numboard", and if numboard[i][j] is zero, board[i][j] is "X".
# C++(12ms)
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if(!board.size())
            return ;
        int row = board.size(),col = board[0].size();
        vector<vector<int>> numboard(row,vector<int>(col));
        for(int i=0;i<row;i++)
            for(int j=0;j<col;j++)
            {
                if(board[i][j] == 'X')
                    numboard[i][j] = 1;
            }
        for(int i=0;i<row;i++)
            for(int j=0;j<col;j++)
            {
                if((i==0 || j==0 || i==row-1 || j == col-1) && (board[i][j] == 'O'))
                {dfs(numboard,i,j,row,col);}
            }
        for(int i=0;i<row;i++)
            for(int j=0;j<col;j++)
                if(numboard[i][j] == 0)
                    board[i][j] = 'X';
    }
    void dfs(vector<vector<int>>& board,int i,int j,int row,int col)
    {
        board[i][j] = -1;
        if(j>0 && board[i][j-1] == 0)
            dfs(board,i,j-1,row,col);
        if(i>0 && board[i-1][j] == 0)
            dfs(board,i-1,j,row,col);
        if(i<row-1 && board[i+1][j] == 0)
            dfs(board,i+1,j,row,col);
        if(j<col-1 && board[i][j+1] == 0)
            dfs(board,i,j+1,row,col);
    }
};
