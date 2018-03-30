## 题目描述
Given two strings representing two complex numbers.
You need to return a string representing their multiplication. Note i2 = -1 according to the definition. 
复数乘法
```
Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
```
## 题目分析
①这个题其实是有bug的，因为按题目要求，中间的运算符“+”是必须要有的，所以钻了这个漏洞，只要把“+”号作为分隔符就可以了。②复数运算公式:(a1+b1i)*(a2+b2i)=(a1*a2-b1*b2)+(a1*b2+a2*b1)i
## Python(34ms)
```python
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1,b1,a2,b2,flag1,flag2=0,0,0,0,1,1
        if a[0]=="-":
            flag1=-1
            a=a[1:]
        if b[0]=="-":
            flag2=-1
            b=b[1:]
        for i in range(len(a)):
            if a[i]!='+':
                a1=a1*10+int(a[i])
            else:
                b1=int(a[i+1:len(a)-1])
                break
        for i in range(len(b)):
            if b[i]!='+':
                a2=a2*10+int(b[i])
            else:
                b2=int(b[i+1:len(b)-1])
                break
        a1*=flag1
        a2*=flag2
        re_a=str(a1*a2-b1*b2)
        re_b=str(a1*b2+a2*b1)
        re=re_a+"+"+re_b+"i"
        return re
```
