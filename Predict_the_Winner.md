## 题目描述
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins. 

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score. 

Example 1:
```
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
```

Example 2:
```
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
```
Note:
1 <= length of the array <= 20. 
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
## 解题思路
一开始就打算采用暴力解法，结果因为理解错误一直没有过还以为是代码出了问题。
如果是B最后拿石头，那么最后的答案是A两种选择中“或”出来的；反之，是B两种选择中“与”出来的（初始假设是“非”的条件下）。
## C++(6ms)
```cpp
class Solution {
public:
    bool helper(vector<int>&nums,int start,int end,int A,int B,bool turn)
    {
        if(start==end)
        {
            if(turn)
                A+=nums[start];
            else
                B+=nums[start];
            return A>=B;
        }
        bool flag=false;
        if(start<end)
        {
            if(turn)
                flag=(helper(nums,start+1,end,A+nums[start],B,!turn)||helper(nums,start,end-1,A+nums[end],B,!turn));
            else
                flag=(helper(nums,start+1,end,A,B+nums[start],!turn)&&helper(nums,start,end-1,A,B+nums[end],!turn));
        }
        return flag;
    }
    bool PredictTheWinner(vector<int>& nums) {
        return helper(nums,0,nums.size()-1,0,0,true);
    }
};
```

## C++(失败代码)
```cpp
class Solution {
private:
    bool flag=0;
public:
    void helper(vector<int>&nums,int start,int end,int A,int B,bool turn)
    {
        if(start==end)
        {
            if(turn)
                A+=nums[start];
            else
                B+=nums[start];
            if(A>=B)flag=1;
        }
        else if(start<end)
        {
            if(turn)
            {
                helper(nums,start+1,end,A+nums[start],B,!turn);
                helper(nums,start,end-1,A+nums[end],B,!turn);
            }
            else{
                helper(nums,start+1,end,A,B+nums[start],!turn);
                helper(nums,start,end-1,A,B+nums[end],!turn);
            }
    }
    }
    bool PredictTheWinner(vector<int>& nums) {
        helper(nums,0,nums.size()-1,0,0,true);
        return flag;
    }
};
```
