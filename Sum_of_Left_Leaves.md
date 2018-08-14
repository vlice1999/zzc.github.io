# Description
Find the sum of all left leaves in a given binary tree.

Example:
```
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
```
# Solution
I made a flag to judge if it is a left node and if the left node hasn't little node, plus it's value.
# C++(0ms)
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
    int re = 0;
public:
    int sumOfLeftLeaves(TreeNode* root) {
        int flag = 0;
        help(root, flag);
        return re;
    }
    void help(TreeNode* node, int flag)
    {
        if(flag && !node->left && !node->right)
            re += node->val;
        if(node)
        {
            if(node->left)
                help(node->left, 1);
            if(node->right)
                help(node->right, 0);
        }
    }
};
```
