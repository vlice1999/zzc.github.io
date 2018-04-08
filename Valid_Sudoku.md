## 题目描述
```
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
```
## 解题思路
分别检查每行每列每个九宫格的数字是否重复。
## Python(251ms)
```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        temp1=[]
        temp2=[]
        for i in range(0,9):
            temp1.append([])
        for i in range(0,9):
            temp2.append([])   
        for i in range(0,9):
            for j in range(0,9):
                temp1[i].append(board[j][i])
        
        k=0
        for i in range(0,9,3):
            for j in range(0,9,3):
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        temp2[k].append(board[row][col])
                k+=1
        print temp2
        
        for i in range(0,9):
            if self.isValid(board[i])==False or self.isValid(temp1[i])==False or self.isValid(temp2[i])==False:
                return False
        return True
    
    def isValid(self,nums):
        temp=[]
        for i in range(0,9):
            if nums[i] not in temp and nums[i]!='.':
                temp.append(nums[i])
                continue
            else:
                if nums[i]=='.':
                    continue
                return False
        return True
```
## C++(28ms)
```cpp
class Solution {
public:
    bool isIn(char &num,vector<char>& temp)
    {
        if(temp.size()==0)return false;
        for(int i=0;i<temp.size();i++)
            if(num==temp[i])
                return true;
        return false;
    }
    
    bool isValid(vector<char>& nums){
        vector<char> temp;
        for(int i=0;i<9;i++)
        {
            if(nums[i]!='.' && isIn(nums[i],temp)==false)
                temp.push_back(nums[i]);
            else
                if(nums[i]!='.')return false;
        }
        return true;
    }
    
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<char>>temp1;
        vector<vector<char>>temp2;
        vector<char>temp;
        
        for(int i=0;i<9;i++)
        {
            temp1.push_back(temp);
            temp2.push_back(temp);
        }
        
        for(int i=0;i<9;i++)
            for(int j=0;j<9;j++)
                temp1[i].push_back(board[j][i]);
        
        int k=0;
        for(int i=0;i<9;i+=3)
            for(int j=0;j<9;j+=3)
            {
                for(int row=i;row<i+3;row++)
                    for(int col=j;col<j+3;col++)
                        temp2[k].push_back(board[row][col]);
                k++;
            }
       
        for(int i=0;i<9;i++)
            if(isValid(board[i])==false||isValid(temp1[i])==false||isValid(temp2[i])==false)return false;
        
        return true;
        
    }
};
```
## 感悟
用C++自己写函数时出现了意想不到的low的错误，还debug了好长时间，真感觉自己傻到家了ε=(´ο｀*)))唉。
