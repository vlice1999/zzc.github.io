## 题目描述

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Example:
```
Input: -3, 0, 3, 4, 0, -1, 9, 2
Output: 45
```
## 解题思路
感觉智商受到了侮辱，不想多说什么。。。。
## C++(23ms)
```cpp
class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int area=(C-A)*(D-B)+(G-E)*(H-F);
        if(A<=E&&E<=C&&C<=G){
            if(F<=B&&B<=H&&H<=D)
                return area-(H-B)*(C-E);
            if(B<=F&&F<=D&&D<=H)
                return area-(D-F)*(C-E);
            if(F<=B&&D<=H)
                return area-(C-E)*(D-B);
            if(B<=F&&H<=D)
                return area-(C-E)*(H-F);
        }
        if(E<=A&&A<=G&&G<=C){
            if(F<=B&&B<=H&&H<=D)
                return area-(H-B)*(G-A);
            if(B<=F&&F<=D&&D<=H)
                return area-(D-F)*(G-A);
            if(F<=B&&D<=H)
                return area-(G-A)*(D-B);
            if(B<=F&&H<=D)
                return area-(G-A)*(H-F);
        }
        if(E<=A&&C<=G)
        {
            if(F<=B&&B<=D&&D<=H)
                return area-(C-A)*(D-B);
            if(B<=F&&F<=H&&H<=D)
                return area-(C-A)*(H-F);
            if(F<=B&&B<=H&&H<=D)
                return area-(C-A)*(H-B);
            if(B<=F&&F<=D&&D<=H)
                return area-(C-A)*(D-F);
        }
        if(A<=E&&G<=C){
            if(F<=B&&B<=D&&D<=H)
                return area-(G-E)*(D-B);
            if(B<=F&&F<=H&&H<=D)
                return area-(G-E)*(H-F);
            if(F<=B&&B<=H&&H<=D)
                return area-(G-E)*(H-B);
            if(B<=F&&F<=D&&D<=H)
                return area-(G-E)*(D-F);
        }
        return area;
    }
};
```
