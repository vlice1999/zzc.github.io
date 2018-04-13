## 题目描述
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element. 
‘’‘
Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

’‘’
## 解题思路
做法太low都不好意思贴代码了，就是设了一个temp数组，存储完了排序。。。
## C++(48ms)
```cpp
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        vector<int>temp;
        for(int i=0;i<matrix.size();i++)
            for(int j=0;j<matrix.size();j++)
                temp.push_back(matrix[i][j]);
        sort(temp.begin(),temp.end());
        return temp[k-1];
    }
};
