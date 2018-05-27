## 题目描述
有一个由1..9组成的数字串.问如果将m个加号插入到这个数字串中,在各种可能形成的表达式中，值最小的那个表达式的值是多少。
## 解题思路
动态规划的例题，视频中已经给了思路，但还是要自己写一下程序的。这个题与之前做的ｌｅｅｔｃｏｄｅ的求最大平方和解题思路完全一样。时间复杂度都是O(n＊n＊m)。

第一种情况：m=0，结果即为这个表达式的值。

第二种情况：m>=n，加号的数量比数字长度还要长，直接返回０吧。

第三种情况：1<=m<=n-1，有递推表达式为re(m,n)=min(re(m-1,i)+M(i+1,n))。

## C++
```cpp
#include <iostream>
#include <string>
using namespace std;

int main(){
        string s;
        int len,m;
        int n;
        cin>>n;
        while(n--){
        cin>>s>>m;
        len=s.size();
        int t=atoi(s.c_str());
        int re[m+2][len+1];
        if(m==0)
        {
                cout << t << endl;
                return 0;
        }
        string c;
        for(int i=0;i<m+2;i++)
                for(int j=0;j<len+1;j++)
                        re[i][j]=100000000;
        for(int i=1;i<=len;i++)
        {
                c=s.substr(0,i);
                t=atoi(c.c_str());
                re[1][i]=t;
                //cout<<t<<" ";
        }
        //cout<<endl;`
        for(int i=2;i<=m+1;i++)
                for(int j=i;j<=len;j++)
                        for(int k=i-1;k<=j;k++)
                        {
                                c=s.substr(k,j-k);
                                re[i][j]=min(re[i-1][k]+atoi(c.c_str()),re[i][j]);
                        }
        cout << re[m+1][len] <<endl;
        }
        return 0;
}
```
