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
