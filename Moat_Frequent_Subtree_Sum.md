## 题目描述
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:
```

  5
 /  \
2   -3
```
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
```
Input:

  5
 /  \
2   -5
```
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
## 解题思路
想多了想多了，其实和[Traingle]('https://github.com/vlice1999/zzc.github.io/blob/master/Triangle.md')是一模一样的题,其实还要简单一些，因为不需要做最优化处理。
## C++(18ms)
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
    map<int,int>Map;
    int max=0;
public:
    void helper(TreeNode* node)
    {
        if(node==NULL)return;
        if(node->left!=NULL)
        {
            helper(node->left);
            node->val+=node->left->val;
        }
        if(node->right!=NULL)
        {
            helper(node->right);
            node->val+=node->right->val;
        }
        Map[node->val]++;
        max=max>Map[node->val]?max:Map[node->val];
    }
    vector<int> findFrequentTreeSum(TreeNode* root) {
        helper(root);
        vector<int>re;
        for(auto it=Map.begin();it!=Map.end();it++)
            if(it->second==max)
                re.push_back(it->first);
        return re;
    }
};
```
