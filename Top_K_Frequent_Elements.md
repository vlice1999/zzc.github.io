## 题目描述
Given a non-empty array of integers, return the k most frequent elements.
For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2]. 
## 问题分析
因为是要返回前k个重复次数最多的数，首先想到了map按value排序。然后按照网上的教程来，然后发现LeetCode中好像不能定义cmp的模板类。然后在网上找到了一个代码，是按桶排序的方式进行排序的。
桶排序：1 2 2 3 4 n(>4)，定义一个长度为n的二维数组nums,nums[i]=i(出现的次数)，再依次从前往后则为升序，反之为降序。根据这个题来看，降序更为方便一些。
## C++(25ms)
```cpp
class Solution {
public:
        
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> bucket(nums.size()+1);
        map<int,int> _map;
        for(int i=0;i<nums.size();i++)
            _map[nums[i]]++;
        map<int,int>::iterator it;
        it=_map.begin();
        while(it!=_map.end())
        {bucket[it->second].push_back(it->first);it++;}
        vector<int> re;
        for(int i=bucket.size()-1;i>0;i--)
            for(int j=0;j<bucket[i].size();j++){
                re.push_back(bucket[i][j]);
                if(re.size()==k)
                    return re;
            }
        return re;
    }
};
```
## 总结体会
最近做了好多关于数组排序的题，算上这个我已经学会的排序方式有冒泡和桶排序，还有就是map和sort了，以及求第K个最大（最小）值的快排方式。
所幸明天没课，哈哈~~~
