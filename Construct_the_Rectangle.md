# Description
For a web developer, it is very important to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
```
1. The area of the rectangular web page you designed must equal to the given target area.

2. The width W should not be larger than the length L, which means L >= W.

3. The difference between length L and width W should be as small as possible.
```
You need to output the length L and the width W of the web page you designed in sequence.
# Solution
Nothing to explain...
# C++(0ms)
```cpp
class Solution {
public:
    vector<int> constructRectangle(int area) {
        int W, L;
        vector<int> re;
        W = sqrt(area);
        int i = 0;
        L = area/W;
        for(i = W;i>=1;i--){
            if(area%i == 0)
            {
                L = area/i;
                re.push_back(L);
                re.push_back(i);
                return re;
            }
        }
        return re;
    }
};
```
