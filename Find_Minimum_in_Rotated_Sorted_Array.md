## 题目描述
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:
```
Input: [3,4,5,1,2] 
Output: 1
```
Example 2:
```
Input: [4,5,6,7,0,1,2]
Output: 0
```
## 解题思路
很明显，这是在诱导我用二分法去做。假如mid>end，说明最小的一定在右边，所以start=mid+1；如果mid<=end，说明最小，一定是在左边，因为mid到end一定是升序排列的。
## C++(5ms)
```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int mid;
        int start=0,end=nums.size()-1;
        while(start!=end){
            mid=(start+end)/2;
            if(nums[end]<nums[mid]){start=mid+1;}
            else
                end=mid;
        }
        return nums[start];
    }
};
```
