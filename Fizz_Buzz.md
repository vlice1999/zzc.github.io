# Description
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
```
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```
# Solution
It's an easy problem, emmmm....
# C++(4ms)
```cpp
class Solution {
public:
    vector<string> fizzBuzz(int n) {
        string tem;
        vector<string> re;
        string str1,str2;
        str1 = "Fizz";
        str2 = "Buzz";
        for(int i = 1;i <= n;i ++){
            tem = "";
            if(i>2 && i%3==0)
                tem = tem+str1;
            if(i>4 && i%5==0)
                tem = tem+str2;
            if(i%3 && i%5)
                tem = to_string(i);
            re.push_back(tem);
        }
        return re;
    }
};
```
