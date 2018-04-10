## 题目描述
```
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. 
Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1) 
Example 2:
coins = [2], amount = 3
return -1. 
```
## 题目分析
找零钱的题和之前的几个题很像（忘了哪些题了），总之每一步都要求得走到当期步数的最小值，即：change[i]=min(change[i],change[i-coins[j]]+1)
## C++(30ms)
```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> change;
        for(int i=0;i<=amount;i++)change.push_back(amount+1);
        change[0]=0;
        for(int i=1;i<=amount;i++)
            for(int j=0;j<coins.size();j++)
                if(coins[j]<=i) change[i]=change[i]<change[i-coins[j]]+1?change[i]:change[i-coins[j]]+1;
        if(change[amount]>amount)return -1;
        return change[amount];
    }
};
```
## Python(2046ms)
```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        change=[0]
        for i in range(amount):
            change.append(amount+1)
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i>=coins[j]:
                    change[i]=min(change[i],change[i-coins[j]]+1)
        
        if change[amount]>amount:
            return -1
        return change[amount]
```
## 总结体会
同一个思路，为什么python就辣么慢！！！
