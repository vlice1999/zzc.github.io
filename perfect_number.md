# description
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
```
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
```
# solution
only a problem need to be noticed, we should get the sqrt of the number, but not half of it.
# c++(0ms)
```cpp
class Solution {

public:

    bool checkPerfectNumber(int num) {

        int sum = 0;

        for(int i = 1;i <= sqrt(num);i ++)

            {

            if(num%i==0)

                sum += (i+num/i);

        }

        sum-=num;

        if(num==0||num==1)

            return false;

        return sum==num;

    }

};
```
