## 题目描述
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:
```
The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
```
Now given N, how many beautiful arrangements can you construct?
## 解题思路
判断是否符合的条件就是(i%index==0 || index%i==0),采用回溯的方法，遍历所有符合这个条件的组合
##Ｃ++(323ms)
```
class Solution {
    private:
    int re=0;
public:
    int countArrangement(int N) {
        vector<int>nums,used;
        for(int i=0;i<N;i++)
            nums.push_back(i+1);
        dfs(used,nums);
        return re;
    }
    void dfs(vector<int>used,vector<int>nums)
    {
        if(nums.size()==0)
            re++;
        int tem=used.size()+1;
        for(int i=0;i<nums.size();i++)
        {
            if(tem%nums[i]==0 || nums[i]%tem==0)
            {
                used.push_back(nums[i]);
                vector<int> new_nums=nums;
                new_nums.erase(new_nums.begin()+i);
                dfs(used,new_nums);
                used.pop_back();
            }
        }
    }
};
```
