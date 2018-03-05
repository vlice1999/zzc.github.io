class Solution(object):              
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        x=0
        o=0
        for i in range(3):
            for j in range(3):
                if board[i][j]=='X':
                    x+=1
                if board[i][j]=='O':
                    o+=1
        n=x-o
        if o>x or x-o>1:
            return False
        num=0
        for i in range(3):
            if board[i].count('X')==3:
                if n==1:
                    num+=1
                else:
                    return False
            if board[i].count('O')==3:
                if n==0:
                    num+=1
                else:
                    return False
            x=0
            o=0
            for j in range(3):
                if board[j][i]=='X':
                    x+=1
                if board[j][i]=='O':
                    o+=1
                if x==3 or o==3:
                    num+=1
        if board[0][0]==board[1][1]==board[2][2]=='X' or board[2][0]==board[1][1]==board[0][2]=='X':
            if n==1:
                num+=1
            else:
                return False
        if board[0][0]==board[1][1]==board[2][2]=='O' or board[2][0]==board[1][1]==board[0][2]=='O':
            if n==0:
                    num+=1
            else:
                return False
        if num>1:
            return False
        else:
            return True
