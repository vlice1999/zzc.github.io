# Description
Count the number of prime numbers less than a non-negative number, n.

Example:
```
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
```
# Solution
It's a easy problem, and I solve it by the stupidest way...
# C++(580ms)
```c++
class Solution {
public:
    int countPrimes(int n) {
        if(n<2)
            return 0;
        int re = 0;
        for(int i=2;i<n;i++)
        {
            int j=2;
            for(;j*j<=i;j++)
                if(i%j==0)
                    break;
            if(j*j>i)
                re++;
        }
        return re;
    }
};
```
