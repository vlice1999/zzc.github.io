## ��Ŀ����
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays
```
Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
```
## ����˼·
Ϊ���ҵ���ͬ����ȵ����ִ���������һ��tem��ά���飬������ʾ��A[i]��B[j]����ͬ������ִ��ĳ��ȡ�����forѭ������A[i]��B[j]��ͬ��ʱ��tem[i][j]=tem[i-1][j-1]+1��
## C++(135ms)
```cpp
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int row=A.size()+1;
        int col=B.size()+1;
        int tem[2][col];
        for(int i=0;i<2;i++)
            for(int j=0;j<col;j++)
                tem[i][j]=0;
        int re=0;
        for(int i=1;i<row;++i)
            for(int j=1;j<col;++j)
            {
                if(A[i-1]==B[j-1])
                    tem[][j]=tem[i-1][j-1]+1;
                re=re>tem[i][j]?re:tem[i][j];
            }
        return re;
    }
};