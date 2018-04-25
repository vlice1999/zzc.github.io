## 题目描述
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
## 题目分析
BST就是左叉的值永远小于右叉的值的二叉树。在n>=2时，在root节点左右两侧共有n-1个数，左右两侧的数都可以在0~n-1的范围内变化。n的组合个数与n的大小没有关系，只和n的数量有关。可得规律re[n]=re[n-1]*re[0]+re[n-2]*re[1]+......+re[0]*re[n-1]。
其中re[0]=1,re[1]=1.
## C++(2ms)
```cpp
class Solution {
public:
    int numTrees(int n) {
        int re[n+1]={0};
        re[0]=1;
        re[1]=1;
        for(int i=2;i<=n;i++)
            for(int j=0;j<i;j++)
                re[i]+=re[i-j-1]*re[j];
        return re[n];
    }
};
```
