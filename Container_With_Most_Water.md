## 题目描述
```
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
给定n个非负整数a1 a2，。a，每个代表一个坐标点(i，ai)。n垂直的线是这样画的，直线i的两个端点在(i，ai)和(i，0)中，找到两条直线，和x轴形成一个容器，这样容器就包含了最多的水。
```
## 解题思路
采用线性时间算法，双指针分别从首尾进行遍历。
## Python(69ms)
```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea=0 #最大面积
        left=0 #左指针
        tmax=0 #最大高度
        right=len(height)-1 #右指针
        while left<right: 
            h=min(height[left],height[right]) #高度
            tmax=max(tmax,h) #最大高度
            maxarea=max((right-left)*h,maxarea) #求最大面积
            while left<right and height[left]<=tmax: left+=1 #如果左指针指的高度小于最大高度，左指针跳过一位
            while left<right and height[right]<=tmax: right-=1 #右指针同上
        return maxarea #返回最大面积
```
## C++(18ms)
```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_area=0;
        int temp_h=0,max_h=0;
        int i=0,j=height.size()-1;
        if(j<=0)return 0;
        while(i<j)
        {
            temp_h=height[i]<height[j]?height[i]:height[j];
            max_h=max_h>temp_h?max_h:temp_h;
            max_area=max_area>temp_h*(j-i)?max_area:temp_h*(j-i);
            while(i<j&&height[i]<=max_h){i++;}
            while(i<j&&height[j]<=max_h){j--;}
        }
        return max_area;
    }
};
```
## 反思
这个题虽然做过一遍，但再做时还是出现了一些问题，比如左指针和右指针是在大于max_h时移动，而不是大于temp_h时移动。因为只有大于max_h时，下一个的面积才有可能比上一个大，同时不造成双指针同时移动。
这个代码还算比较成功的，毕竟超过了97.63%的人(#^.^#)
