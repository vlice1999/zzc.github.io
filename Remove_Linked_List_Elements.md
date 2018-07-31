# Description
Remove all elements from a linked list of integers that have value val.

Example:
```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```
# Solution
A easy and old problem, and the only difficulty is to process the last node. 
# C++()
```c++
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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* cur = new ListNode(0);
        cur->next = head;
        ListNode* point = cur;
        while(point != NULL){
            if(point->next && point->next->val == val )
                point->next =point->next->next;
            else
                point = point->next;
        }
        return cur->next;
    }
};
```
