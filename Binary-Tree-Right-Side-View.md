## 题目描述
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
```
For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

You should return [1, 3, 4]. 
```
## 解题思路
简单粗暴，搜索出每层所有元素，然后提取每层最右边那个
## C++(5ms)
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
    vector<int> rightSideView(TreeNode* root) {
         vector<vector<int>>res;
        vector<int>temp;
        if(root==NULL)return temp;
        res.push_back(temp);
        search(root,1,res);
        for(int i=0;i<res.size();i++){
            int l=0;
            l=res[i].size();
            temp.push_back(res[i][l-1]);
        }
        return temp;
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
## Python(52ms)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def search(self,node,depth,temp):
        if depth==len(temp):
            temp.append([])
        if node.left!=None:
            temp[depth].append(node.left.val)
            self.search(node.left,depth+1,temp)
        if node.right!=None:
            temp[depth].append(node.right.val)
            self.search(node.right,depth+1,temp)
            
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        re=[]
        temp=[[root.val]]
        self.search(root,1,temp)
        for i in range(len(temp)):
            l=len(temp[i])
            if l!=0:
                re.append(temp[i][l-1])
        return re
```
