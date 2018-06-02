## 题目描述
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:
```
Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
```
Example 2:
```
Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
```
## 解题思路
一开始打算用map，发现其实map一点也不方便～

用int数组就足够了。一开始先赋值0，走过的room就赋值1，等到所有的room都赋值1。flag设为true就可以了。
## C++(16ms)
```cpp
class Solution {
private:
    bool flag=0;
public:
    void helper(vector<vector<int>>& rooms,int room,int step[],int len)
    {
        if(room>=rooms.size()||flag==1)
            return;
        for(int i=0;i<rooms[room].size();i++)
        {      
            int num=0;
            if(step[rooms[room][i]]==0){
                step[rooms[room][i]]=1;
                helper(rooms,rooms[room][i],step,len);
            }
            else
            {
                int i=0;
                for(;i<len;i++)
                    if(step[i]==0)
                        break;
                if(i==len-1)
                {flag=1;return;}
            }
        }
        int i=0;
        for(;i<len;i++)
            if(step[i]==0)
                return;
        flag=1;
    }
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int len=rooms.size();
        int step[len]={0};
        step[0]=1;
        helper(rooms,0,step,len);
        return flag;
    }
};
```
