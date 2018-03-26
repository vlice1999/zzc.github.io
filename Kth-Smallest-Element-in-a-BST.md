## 题目描述
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
给一个BST（二叉查询数），返回其中第k小的数
## 题目分析
好久没写题目分析了。这个题一开始不知道BST是啥，就随便向测试中输入几个数测试，发现得不到想要的结果。查了BST的意思后才知道原来内置的测试程序只是用来找BST的第k小的数的。
BST的意思就是每个节点的左节点及其以下节点的值比它小，右节点及其以下的值比它大。所以递归的时候先指向左节点就可以了，存值，再指向右节点就可以了。
## C++(16ms)
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
    vector<int>nums;
    void search(TreeNode* node){
        if(node!=NULL){
            search(node->left);
            nums.push_back(node->val);
            search(node->right);
        }
    }
    int kthSmallest(TreeNode* root, int k) {
        search(root);
        return nums[k-1];
    }
};
```
## Python(93ms)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        Solution.re=[]
        self.search(root)
        return Solution.re[k-1]
    def search(self,node):
        if(node!=None):
            self.search(node.left)
            Solution.re+=[node.val]
            self.search(node.right)
```
## 总结体会
这个算法貌似比较慢，因为用到了递归，应该可以用循环代替，白天再想想吧。。。
白天玩的太过了，搞得晚上睡这么晚，下次应该先写作业再看电影的(*/ω＼*)
