# Description
Given two arrays, write a function to compute their intersection.


Example:
```
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
```
# Solution
I think, the map container can do anything. emmm...
# C++(4ms)
```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> nums;
        for(int i=0;i < nums1.size(); i++)
        {
            if(nums[nums1[i]] == 0)
                nums[nums1[i]] = 1;
        }
        vector<int> re;
        for(int i=0;i < nums2.size(); i++)
        {
            if(nums[nums2[i]]){
                re.push_back(nums2[i]);
                nums[nums2[i]] = 0;
            }
        }
        return re;
    }
};
```
