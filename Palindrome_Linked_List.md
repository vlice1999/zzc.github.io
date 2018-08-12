# Description

Given a singly linked list, determine if it is a palindrome.

Example 1:
```
Input: 1->2
Output: false
```
Example 2:
```
Input: 1->2->2->1
Output: true
```
# Solution
I used an array to store every number and used two pointers to judge if the array is a palindrome.
# C++(12ms)
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(!head)
            return true;
        vector<int> nums;
        while(head->next){
            nums.push_back(head->val);
            head = head->next;
        }
        nums.push_back(head->val);
        for(int i = 0, j = nums.size()-1; i<j; i++, j--)
        {
            if(nums[i]!=nums[j])
                return false;
        }
        return true;
    }
};
```
