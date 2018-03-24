## 题目描述
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).
```
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
```
## 解题思路
直接遍历出所有节点，然后将数组中下标为奇数的数组反转。
## C++(4ms)
```cpp
#include <queue> //用到了reverse函数  
#include<algorithm>  
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>>re;
        if(root==NULL)return re;
        vector<int>temp;
        re.push_back(temp);
        search(root,0,re);
        for(int i=0;i<re.size();i++){
            if(i%2==0){
                reverse(re[i].begin(),re[i].end());
            }
        }
        return re;
    }
    void search(TreeNode* node,int depth,vector<vector<int>>& re){
        if(node==NULL)return ;
        if(depth>=re.size()){
                vector<int>temp;
                re.push_back(temp);}
        re[depth].push_back(node->val);
        search(node->right,depth+1,re);
        search(node->left,depth+1,re);
    }
};
```
## Python(48ms)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def search(self,node,depth):
        if depth>=len(Solution.re):
            Solution.re.append([])
        if node!=None:
            Solution.re[depth]+=[node.val]
            if node.left!=None:
                self.search(node.left,depth+1)
            if node.right!=None:
                self.search(node.right,depth+1)
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        Solution.re=([])
        if root==None:
            return [];
        self.search(root,0)
        for i in range(len(Solution.re)):
            if i%2!=0:
                Solution.re[i]=Solution.re[i][::-1]
        return Solution.re
```
