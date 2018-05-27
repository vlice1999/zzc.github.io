## 题目描述
We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
```
Input: 
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation: 
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
```
## 解题思路
首先double一个二维数组，用来记录前Ｎ个数分成ｋ个部分时候的最大均值。然后进行三层循环，递推公式为dp[i][k]=max(dp[i][k],dp[i-k~i][k-1]+(dp[i][k]×i-dp[j][k]×j)/(i-j)).

## C++(9ms)
```cpp
class Solution {
public:
    double largestSumOfAverages(vector<int>& A, int K) {
        int len=A.size();
        double dp[len+1][K+1]={0.0,0.0};
        for(int i=1;i<=len;i++)
            dp[i][1]=(dp[i-1][1]*(i-1)+A[i-1])/i;
        
        for(int k=2;k<=K;k++)
            for(int i=k;i<=len;i++)
                for(int j=k-1;j<i;j++)
                    dp[i][k]=max(dp[i][k],dp[j][k-1]+(dp[i][1]*i-dp[j][1]*j)/(i-j));
        
        return dp[len][K];
    }
};
```
## python(522ms)
```py
class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        dp=[[0.0 for i in range(K+1)] for j in range(len(A)+1)]
        for i in range(1,len(A)+1):
            dp[i][1]=(A[i-1]+dp[i-1][1]*(i-1))/i
            print dp[i][1]
        for k in range(2,K+1):
            for i in range(k,len(A)+1):
                for j in range(k-1,i):
                    dp[i][k]=max(dp[i][k],dp[j][k-1]+(dp[i][1]*i-dp[j][1]*j)/(i-j))
        
        return dp[len(A)][K]
```
