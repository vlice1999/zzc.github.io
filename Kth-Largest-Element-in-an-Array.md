## 题目描述
```
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element. 
For example,
Given [3,2,1,5,6,4] and k = 2, return 5. 
```
## 解题思路
因为今天要赶高数作业，只好先打卡了。
这个题我用了最简单的方法，就是排序后再去找值。这个看似简单的问题竟然有655个赞，查过之后发现原来有四种解法。因为要赶作业，所以明天再仔细看看吧(*/ω＼*)。
## C++(12ms)
```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        return nums[(nums.size())-k];
    }
};
```
## Python(43ms)
```python
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)-k]
```
