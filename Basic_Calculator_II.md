# Description
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
```
Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
```
# Solution
At first, I tried to solve it by normal way and only one train data can't be solve because it's too long. So, I used a line of code to solve this problem.
# Python(the normal code)
```python
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
     
        punc,num = [],[]
        tem = 0
        start,end =-1 , -1
        for i in range(len(s)):
            if s[i]=='/' or s[i]=='*' or s[i]=='+' or s[i]=='-':
                punc.append(s[i])
                start = end+1
                end = i
                num.append(int(s[start:end]))
        
        num.append(int(s[end+1:]))
        if(len(num) == 1):
            return num[0]
        L = len(punc)
        i = 0
        tem = 0
        while i < L:
            if punc[i] == '*':
                num[i+1] = int(num[i]*num[i+1])
                num.remove(num[i])
                punc.remove(punc[i])
                i -= 1
                L -= 1
            
            elif punc[i] == '/':
                num[i+1] = int(num[i]/num[i+1])
                num.remove(num[i])
                punc.remove(punc[i])
                i -= 1
                L -= 1
            tem = max(tem,num[i])
            i+=1
        print(tem)
        for i in range(len(punc)):
            if punc[i] == '+':
                num[i+1] += num[i]
            if punc[i] == '-':
                num[i+1] = num[i] - num[i+1]
           
        return num[len(num)-1]
```
# Python(128ms)
```python
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return eval(s.replace('/','//'))
```
