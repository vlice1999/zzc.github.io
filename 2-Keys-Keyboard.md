## 题目描述
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step: 
Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'. 
```
Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
```
## Python（1211ms）
```python
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[]
        for i in range(n+1):
            dp.append(n+1)
        dp[0]=dp[1]=0
        for i in range(2,n+1):
            for j in range(1,i):
                if i%j==0:
                    dp[i]=min(dp[i],dp[j]+i/j)
        
        return dp[n]
```
