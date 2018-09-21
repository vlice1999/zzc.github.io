# Description
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 
For example:
```
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
 
return [2].
```
# C++(16 ms)
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
    map<int, int> re;
public:
    vector<int> findMode(TreeNode* root) {
        vector<int> tem;
        if(root == NULL)
            return tem;
        helper(root);
        auto it = re.begin();
        
        int max_num = 0;
        while(it != re.end()){
            max_num = max(max_num, it->second);
            it ++;
        }
        it = re.begin();
        while(it != re.end()){
            if(it -> second == max_num)
                tem.push_back(it->first);
            it++;
        }
        return tem;
    }
    
    void helper(TreeNode* node){
        if(node != NULL){
            re[node->val] ++;
        }
        if(node->left != NULL)
            helper(node -> left);
        if(node->right != NULL)
            helper(node -> right);
    }
};
```
