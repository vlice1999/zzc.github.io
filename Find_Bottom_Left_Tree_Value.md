## 题目描述
Given a binary tree, find the leftmost value in the last row of the tree.
Example 1:
```
Input:

    2
   / \
  1   3

Output:
1
```
Example 2: 
```
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
```
## 解题思路
只要保证在更深深度时更新re就好了。
## C++(12ms)
```cpp
**
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
    int re=0;
    int depth=0;
public:
    void dfs(TreeNode* node,int dep)
    {
        if(dep>depth&&node!=NULL)
        {re=node->val;depth=dep;}
        if(node->left!=NULL)
            dfs(node->left,dep+1);
        if(node->right!=NULL)
            dfs(node->right,dep+1);
    }
    int findBottomLeftValue(TreeNode* root) {
        if(root==NULL)
            return re;
        re=root->val;
        if(root->left!=NULL)
            dfs(root->left,2);
        if(root->right!=NULL)
            dfs(root->right,2);
        return re;
    }
};
```
