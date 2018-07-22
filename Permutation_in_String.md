# Description
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
```
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
```
# Solution
If s2 can contains the permutation of s1, it will only contain s1's letters in a part of itself.So if find a letter in s1 but not in s2, we fill find again from this position. Besides, the numbers of every letter will be same between s1 and s2 in the same length. If find certain letter's numbers in s2 is more than s1, we should recount from the first position of this letter.
# C++(4ms)
```c++
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int dict[26] = {0},nums=0,slow_point=0;
        for(int i=0;i<s1.size();i++)
            dict[s1[i]-'a']++;
        for(int i=0;i<s2.size() && nums<s1.size();i++)
        {
            if(dict[s2[i]-'a']){
                dict[s2[i]-'a']--;
                nums++;
            }
            else
                while(s2[slow_point++] != s2[i]){
                    ++dict[s2[slow_point-1]-'a'];
                    nums--;
                }
        }
        return (nums == s1.size());
    }
};
```
#C++(loser)
```c++
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        map<char,int> dict_1;
        int num1,num2;
        for(int i=0;i<s1.size();i++)
            dict_1[s1[i]]++;
        int slow_point =0,fast_point = slow_point + s1.size();
        while(fast_point <= s2.size()){
            map<char,int> dict_2,pos;
            int i=slow_point,nums = 0;
            for(;i<fast_point;i++){
                if(pos[s2[i]] <= slow_point)
                    pos[s2[i]] = i+1;
                dict_2[s2[i]] ++;
                nums ++;
                num2 = dict_2[s2[i]];
                #cout << s2[i] <<" "<< num2 <<endl;
                num1 = dict_1[s2[i]];
                if(num1==0){
                    slow_point = i+1;
                    fast_point = slow_point + s1.size();
                    break;
                }
                if(num2>num1)
                {
                    for(int j = slow_point; j <pos[s2[i]];j++)
                    {dict_2[s2[j]-1]--;fast_point++;nums--;}
                    slow_point = pos[s2[i]];
                    pos[s2[i]] = i+1;
                }
            }
            if(i == fast_point && nums == s1.size())
                return true;
        }
        return false;
    }
};
```
# Summary
My first code is wrong, then I find a correct solution's thinking is same to me but it counts by subtraction.   
