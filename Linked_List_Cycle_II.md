## 题目描述
```
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list.
给出一个链表，返回链表环的起点。没有环的话，返回null(注：不使用额外的空间)
```
## 解题思路
①判圈算法：使用双指针，一个快指针和一个慢指针同时遍历，如果遇到快指针与慢指针相同的情况，说明存在链表环。如果遇到指针为空的情况，则不存在链表环
②因为快指针速度是慢指针的二倍，而当两指针相遇时，快指针比慢指针快一个链表环的长度。
## Python(76ms)
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        p1=head
        p2=head
        l1=0
        l2=0
        while p1.next!=None:
            p1=p1.next.next
            l1+=2
            if p1==None:
                return None
            if p1==p2:
                l=l1-l2
                temp=head
                p=head
                for i in range(0,l):
                    p=p.next
                while temp.next!=None:
                    if temp==p:
                        return p
                    else:
                        temp=temp.next
                        p=p.next
            else:
                p2=p2.next
                l2+=1
        return None
```
## C++(18ms)
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
    ListNode *detectCycle(ListNode *head) {
        int l1=0,l2=0;
        if(head==NULL) return NULL;
        ListNode *fast=head,*slow=head;
        while(fast->next && fast->next->next)
        {
            l1+=2,l2+=1;
            fast=fast->next->next;
            slow=slow->next;
            if(fast==slow)
            {
               int l=l1-l2;
               ListNode *temp=head;
               while(l>0)
               {
                   temp=temp->next;
                   l--;
               }
                while(head!=temp)
                {
                    head=head->next;
                    temp=temp->next;
                }
                return head;
            }
        }
    return NULL;
    }
};
```
## C++(10ms) ***别人家的代码***
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
    ListNode *detectCycle(ListNode *head) {
        int l1=0,l2=0;
        if(head==NULL) return NULL;
        ListNode *fast=head,*slow=head;
        while(fast->next && fast->next->next)
        {
            l1+=2,l2+=1;
            fast=fast->next->next;
            slow=slow->next;
            if(fast==slow)
            {
                fast=head;
                while(fast!=slow)
                {
                    fast=fast->next;
                    slow=slow->next;
                }
                return fast;
            }
        }
    return NULL;
    }
};
```
## 反思
这个题我本来是抱着轻松愉快的心情复习的，结果看见了网上的一个代码，思考了半天还是没弄清楚为什么慢指针没走的剩余环的长度会是环的起点到链表开头的长度。
