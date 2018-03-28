## 题目描述
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s. 
```
For example, given s = "aab",
Return 
[
  ["aa","b"],
  ["a","a","b"]
]
```
## 题目分析
因为是要输出所有可能的回文字符串组合，不自觉的就想到了回溯，遍历所有可能的组合。
## Python(184ms)
```python
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.re=[]
        self.search(s,[])
        return Solution.re
    def search(self,s,temp):
        if len(s)==0:
            Solution.re.append(temp)
        for i in range(1,len(s)+1):
            if s[:i]==s[:i][::-1]:
                self.search(s[i:],temp+[s[:i]])
```
