## 题目描述
We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?
```
Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100 
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.
Notes:

1 <= difficulty.length = profit.length <= 10000
1 <= worker.length <= 10000
difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
```
## 解题思路
首先定义一个长度为100001的数组a[]，表示在当前难度下获得的最大利润。第一步就是先根据所给数据，下标为难度，值为利润，存放元素。第二步是填充整个数组，确保在worker范围内难度对应a都有利润值，最后求和。需要注意的是，工作的难度和利润会有重复，所以一定要向a中存放当前难度利润的最大值。
## C++(113ms)
```cpp
class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        int a[100001]={},d,p;
        for(int i=0;i<difficulty.size();i++)
        {
            d=difficulty[i];
            p=profit[i];
            a[d]=max(a[d],p);
        }
        for(int i=1;i<100001;i++)
            a[i]=max(a[i],a[i-1]);
        int sum=0,tem;
        for(int i=0;i<worker.size();i++)
        {
            tem=worker[i];
            sum+=a[tem];
        }
        return sum;
    }
};
```
