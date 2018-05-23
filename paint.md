## 题目描述
有一个正方形的墙，由N×N个正方形的砖组成，其中一些砖是白色的，另外一些砖是黄色的。Bob是个画家，想把全部的砖都涂成黄色。但他的画笔不好使。当他用画笔涂画第(i, j)个位置的砖时， 位置(i-1, j)、 (i+1, j)、 (i, j-1)、 (i, j+1)上的砖都会改变颜色。请你帮助Bob计算出最少需要涂画多少块砖，才能使所有砖的颜色都变成黄色。
## 题目要求
输入：

第一行是个整数t(1≤t ≤20)，表示要测试的案例数。然后是t个案例。每个案例的首行是一个整数n (1≤n ≤15)，表示墙的大小。接下来的n行表示墙的初始状态。每一行包含n个字符。第i行的第j个字符表示位于位置(i,j)上的砖的颜色。“w”表示白砖，“y”表示黄砖。

输出：

每个案例输出一行。如果Bob能够将所有的砖都涂成黄色，则输出最少需要涂画的砖数，否则输出“inf”。

## 解题思路
枚举的例题，昨天弄明白了熄灯问题的解题过程，本来以为这个题写的时候会很顺畅，但是因为种种不注意，最后花了三个小时才改好。

这个题和熄灯问题几乎是一样的，不同之处在于，熄灯问题要求遍历所有的组合，而且给的数组是固定的＝——＝。

首先看一下熄灯问题，原题的解决方案分为三部分:guess(),enumerate(),和main()，其中enumerate()是用来枚举的，枚举的方法是运用二进制的加法，依次枚举；guess()是用来判断解决方案是否合理的，判断的条件是看最后一行是否熄灭了。

熄灯问题中假定有解，这个问题中没有假定，所以需要达到第一行都被画时才可以停止。而怎么判断是否有解呢？一开始尝试在ｅｎｕｍｅｒａｔｅ中计数并判断，然后失败了。看了网上的一个博文后，在ｇｕｅｓｓ中边判断边计数，如果不符合解决方案的要求时候，返回一个１００１，这时候的re可以设为全局变量，这样在最后，如果re=1001的话，就说明无解了。

## C++
```cpp
#include <iostream>
using namespace std;
void enumerate();
int guessCount();
int re,len,press[20][20],puzzle[20][20];
int main(){
        int N;
        cin>>N;
        while(N--)
        {
                cin>>len;
                char c;
                for(int i=0;i<len+1;i++)
                        for(int j=0;j<len+1;j++)
                                press[i][j]=puzzle[i][j]=0;
                for(int i=1;i<len+1;i++)
                        for(int j=1;j<len+1;j++){
                                cin>>c;
                                if(c=='w')
                                        puzzle[i][j]=1;
                        }
                re=1001;
                enumerate();
                if(re>1000)
                        cout<<"inf"<<endl;
                else
                        cout<<re<<endl;
        }
        return 0;
}
int guessCount(){
        int tem=0;
        for(int i=1;i<len;i++)
                for(int j=1;j<len+1;j++)
                        press[i+1][j]=(puzzle[i][j]+press[i][j]+press[i-1][j]+press[i][j+1]+press[i][j-1])%2;
        for(int i=1;i<len+1;i++)
                if((press[len-1][i]+press[len][i+1]+press[len][i-1]+press[len][i])%2!=puzzle[len][i])
                        return 1001;
        for(int i=1;i<len+1;i++)
                for(int j=1;j<len+1;j++)
                        if(press[i][j]==1)
                                tem++;
        return tem;
}

void enumerate(){
        int c=1,min=0;
        while(press[1][len+1]<1)
        {
                min=guessCount();
                if(min<re)
                        re=min;
                press[1][1]++;
                c=1;
                while(press[1][c]>1)
                {
                        press[1][c]=0;
                        c++;
                        press[1][c]++;
                }
        }
}
```
## 解题感悟
昨天开始看的算法，本来以为做过这么多leetcode的题做起来会更轻松一些，然而第一节课的枚举就让我头疼不已。枚举相比回溯，似乎更难掌握一些，回溯只要一直递归就可以了，判断条件一般不会很复杂，而枚举的题，判断条件看起来是真不好弄。后面还有一个“拨钟问题”，明天再想想看能写出来吧。
