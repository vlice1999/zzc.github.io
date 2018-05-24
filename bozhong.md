## 题目描述
有一个３＊３个时钟，指在不同时间。

现在需要用最少的移动，将9个时钟的指针都拨到12点的位置。共允许有9种不同的移动。如下表所示，每个移动会将若干个时钟的指针沿顺时针
方向拨动90度。
```
移动 影响的时钟 
1 ABDE
2 ABC
3 BCEF
4 ADG
5 BDEFH
6 CFI
7 DEGH
8 GHI
9 EFHI
```

## 题目要求
输入：

从标准输入设备读入9个整数，表示各时钟指针的起始位置。0=12点、1=3点、2=6点、3=9点。

输出：

输出一个最短的移动序列，使得9个时钟的指针都指向12点。按照移动的序号大小，输出结果。
## C++
```cpp
//暴力枚举法，过多不解释

#include <iostream>
using namespace std;

int main(){
        int a,b,c,d,e,f,g,h,i;
        int re[9]={0},min=100000,t=0;
        cin>>a>>b>>c>>d>>e>>f>>g>>h>>i;
        for(int i1=0;i1<4;i1++)
                for(int i2=0;i2<4;i2++)
                        for(int i3=0;i3<4;i3++)
                                for(int i4=0;i4<4;i4++)
                                        for(int i5=0;i5<4;i5++)
                                                for(int i6=0;i6<4;i6++)
                                                        for(int i7=0;i7<4;i7++)
                                                                for(int i8=0;i8<4;i8++)
                                                                        for(int i9=0;i9<4;i9++){
                if((a+i1+i2+i4)%4==0&&(b+i1+i2+i3+i5)%4==0&&(c+i2+i3+i6)%4==0&&(d+i1+i4+i5+i7)%4==0&&(e+i1+i3+i5+i7+i8)%4==0&&(f+i3+i6+i5+i9)%4==0&&(g+i4+i7+i8)%4==0&&(h+i5+i7+i8+i9)%4==0&&(i+i6+i8+i9)%4==0)
                {
                        t=i1+i2+i3+i4+i5+i6+i7+i8+i9;
                        if(t<min)
                        {
                                cout<<i1<<" "<<i2<<" "<<i3<<" "<<i4<<" "<<i5<<" "<<i6<<" "<<i7<<" "<<i8<<" "<<i9<<endl;
                                min=t;
                                re[0]=i1;re[1]=i2;re[2]=i3;re[3]=i4;re[4]=i5;re[5]=i6;re[6]=i7;re[7]=i8;re[8]=i9;
                        }
                }
                                                                        }
        for(int i=0;i<9;i++)
                if(re[i]!=0)
                        cout<<i+1<<" ";
        return 0;
}
```
