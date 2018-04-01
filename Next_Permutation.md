## 题目描述
```
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.
在不申请额外空间的情况下将nums数组中的数字重新排序，新构成的“数字”是所有可能的“数字”中比当前“数字”大的最小的。
如果不存在这个“数字”，返回nums重新排序后的最小“数字”。
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```
## 题目分析
①不需要返回任何值②在不申请额外空间的情况下改变nums数组顺序
## 解题思路
我是从后向前遍历，找到第一个降序数字。将其之后的数字重新排序，找到第一个比其大的数字进行交换，然后重新整合nums数组。
## Python(87ms)
```python
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=len(nums)-1
        max=nums[l]
        l-=1
        while l>=0:
            if nums[l]>=max: 
                max=nums[l]
            else:
        #这里不知道算不算是申请了额外空间
                temp=nums[l:] 
                temp.sort()
                i=0
                for i in range(len(temp)):
                    if temp[i]>nums[l]:
                        nums[l]=temp[i]
                        temp=temp[:i]+temp[i+1:]
                        for k in range(len(temp)):
                            n=nums[l+k+1]
                            nums[l+k+1]=temp[k]
                        break
                break
            l-=1
        if l==-1:
            nums=nums.sort()
```
## C++(18ms)
```cpp
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len=0,temp;
        len=nums.size();
        if(len==0||len==1)return;
        int pos;
        pos=len-1;
        while(pos>0){if(nums[pos-1]<nums[pos])break;pos--;}
        if(pos==len-1)
        {
            temp=nums[pos-1];
            nums[pos-1]=nums[pos];
            nums[pos]=temp;
            return;
        }
        if(pos==0){sort(nums.begin(),nums.end());return;}
        for(int i=pos;i<len;i++)
        {
            if(nums[i]<=nums[pos-1])
            {
                temp=nums[i-1];
                nums[i-1]=nums[pos-1];
                nums[pos-1]=temp;
                break;
            }
            if(i==len-1){
                temp=nums[i];
                nums[i]=nums[pos-1];
                nums[pos-1]=temp;
                break;
            }
        }
        cout<<nums[0]<<nums[1]<<nums[2];
        sort(nums.begin()+pos,nums.end());
        return;
    }
};
```
## 反思与感悟
最近几天做leetcode做的很吃力，一方面可能是因为事情多，不能好好去思考，更深层次的原因应该是我的知识量已经不够了。
所以接下来的一周不准备做新题，将之前做过的题感觉不大熟的用C++再刷一遍，同时学习一下数据结构，扩展一下知识面。可以顺便用博客园做做数据结构的笔记，O(∩_∩)O哈哈~
