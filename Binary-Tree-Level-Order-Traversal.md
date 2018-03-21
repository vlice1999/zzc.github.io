## 题目描述
```
Pick One

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
```
## C++(7ms)
```cpp
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>res;
        if(root==NULL)return res;
        vector<int>temp;
        res.push_back(temp);
        search(root,1,res);
        return res;
    }
    void search(TreeNode* node,int depth,vector<vector<int>>& re){
        if(depth>re.size()){vector<int>temp;re.push_back(temp);}
        if(node==NULL)return;
        else{
            re[depth-1].push_back(node->val);
            if(node->left!=NULL)search(node->left,depth+1,re);
            if(node->right!=NULL)search(node->right,depth+1,re);
        }
    }
};
```
## Python(66ms)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def search(self,node,depth):
        if node==None:
            return
        if depth>len(Solution.re):
            Solution.re.append([])
        if node!=None:
            Solution.re[depth-1]+=[node.val]
            if node.left!=None:
                self.search(node.left,depth+1)
            if node.right!=None:
                self.search(node.right,depth+1)
            
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        Solution.re=[]
        self.search(root,1)
        return Solution.re
```
## 解题收获
还是第一次尝试用C++去解决二叉树的题，貌似运行速度比Python快好多。。。
