## 题目描述
In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.
Return the minimum number of rabbits that could be in the forest.
```
Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
```
## 题目分析
题目的意思就是数清楚森林中有多少的rabbits。每个兔子都说这个森林中有多少兔子和它颜色相同。当然，兔子的消息都是可靠的。
假如answers[i]=0，那么这只兔子就是森林中最个性的色彩（re+=1）。如果是[1,1]这种情况，那么假定这两只兔子颜色相同，即这种颜色的兔子有两只。[1,1,1]这种情况，即为2+1+1.
## 解决方案
先排序，然后遍历所有兔子。令num=answers[i],tem=num,re+=num;在tem的长度内，如果answers[i]==num并且tem>=0,i++;否则，跳出小循环。
## C++(6ms)
```cpp
class Solution {
public:
    int numRabbits(vector<int>& answers) {
        int len=answers.size();
        sort(answers.begin(),answers.end());
        int tem,re=0,i=0,num;
        while(i<len)
        {
            while(answers[i]==0){re++;i++;}
            num=answers[i];
            re+=(num+1);
            tem=num;
            while(answers[i]==num && tem>=0)
            {
                i++;
                tem--;
            }
        }
        return re;
    }
};
```
