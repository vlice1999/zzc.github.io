# Description
You need to find the largest value in each row of a binary tree.


Example:
```
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

```
# Solution
I used a simple method to solve this problem. First, use an array to store every number. Then, use for-loop to find the maximum number in every row and store it. 
# C++(8ms)
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
    vector<vector<int>> tem;
public:
    vector<int> largestValues(TreeNode* root) {
        vector<int> re;
        if(root == NULL)
            return re;
       
        help(root, 0);
        for(int i = 0;i<tem.size();i ++){
            re.push_back(tem[i][0]);
            for(int j = 1;j <tem[i].size();j ++){
                re[i] = max(re[i], tem[i][j]);
            }
        }
        return re;
    }
    
    void help(TreeNode* root, int depth){
        if(tem.size() <= depth)
        {
            vector<int> t;
            t.push_back(root -> val);
            tem.push_back(t);
        }
        else{
            tem[depth].push_back(root->val);
        }
        
        if(root->left != NULL)
            help(root->left, depth+1);
        if(root->right != NULL)
            help(root->right, depth+1);
    }
};
```
