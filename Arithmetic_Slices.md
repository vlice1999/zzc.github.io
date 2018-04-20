## 题目描述
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
```
For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7
```
```
Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

```
题目描述太复杂了，直白点，就是找出数组中连续等差数列的个数。
## 解题思路
双for循环，外层循环控制新数组的起点，内层循环用来判断等差数列。满足等差数列两个条件即可：等差，个数大于3.
## C++(4ms)
```cpp
#include<iostream>
#include<vector>
#include<algorithm>
#include<sstream>
using namespace std;
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
    //填充的代码
        int re=0;
        int t;
        if(A.size()<3)
            return re;
        for(int i=0;i<A.size()-2;i++)
        {
            t=A[i+1]-A[i];
            vector<int> tem;
            tem.push_back(A[i]);
            for(int j=i+1;j<A.size();j++)
            {
                if(A[j]-A[j-1]==t)tem.push_back(A[j]);
                else
                    break;
                if(tem.size()>=3)re++;
                            }
        }
        return re;
    //代码填充结束
    }
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

int main() {
    string line;
    while (getline(cin, line)) {
    vector<int> A = stringToIntegerVector(line);

        int ret = Solution().numberOfArithmeticSlices(A);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}
```
