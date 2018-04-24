## 题目描述
Given a binary tree, return the inorder traversal of its nodes' values.
```
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```
## 解题思路
直接递归的。。。搜索的时候先搜索左节点，存值后搜索右节点。
## C++(3ms)
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
private:
    vector<int>result;
    void Node(TreeNode* node){
        if(node==NULL)
            return;
        Node(node->left);
        result.push_back(node->val);
        Node(node->right);
    }
public: 
    vector<int> inorderTraversal(TreeNode* root) {
        Node(root);
        return result;
    }
};
```
