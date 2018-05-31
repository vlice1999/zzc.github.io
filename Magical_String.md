## 题目描述
```
```
## 解题思路
其实吧，这个题直接快慢指针遍历了，虽然通过了，但感觉字符串实际上是不对的。

中间处理了一下快指针等于２的特殊情况，这时候快慢指针在同一位置，慢指针指在２上。但是这时候不是增加两个１，而是要重复一次２。

用vector<int>需要10ms，相同思路，int需要7ms。
## C++(10ms)
```cpp
//vevtor<int>
class Solution {
public:
    int magicalString(int n) {
        if(n==1)return 1;
        if(n==0)return 0;
        int rec=1;
        vector<int> re={1};
        for(int i=0,j=0;i<n;j++)
        {
            if(re[j]==1)
            {
                if(re[i]==1)
                    re.push_back(2);
                else
                {
                    re.push_back(1);
                    if(i<n-1)
                        rec++;
                }
                i++;
            }
            else if(re[j]==2){
                if(i==1)
                {
                    re.push_back(2);
                    i++;
                    continue;
                }
                if(re[i]==1){
                    re.push_back(2);
                    re.push_back(2);
                }
                if(re[i]==2){
                    re.push_back(1);
                    re.push_back(1);
                    if(i<n-2)rec+=2;
                    if(i==n-2)rec++;
                }
                i+=2;
            }
        }
        return rec;
    }
};
```
## C++(7ms)
```
//int
class Solution {
public:
    int magicalString(int n) {
        if(n==1)return 1;
        if(n==0)return 0;
        int rec=1;
        int re[100001];
        for(int i=0;i<=n;i++)
            re[i]=1;
        for(int i=0,j=0;i<n;j++)
        {
            if(re[j]==1)
            {
                if(re[i]==1)
                    re[i+1]=2;
                else
                    if(i<n-1)
                        rec++;
                i++;
            }
            else if(re[j]==2){
                if(i==1)
                {
                    re[i+1]=2;
                    i++;
                    continue;
                }
                if(re[i]==1){
                    re[i+1]=2;re[i+2]=2;
                }
                if(re[i]==2){
                    if(i<n-2)rec+=2;
                    if(i==n-2)rec++;
                }
                i+=2;
            }
        }
        return rec;
    }
};
```
