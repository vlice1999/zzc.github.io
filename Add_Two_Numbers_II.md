## 题目描述
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
```
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
```

## 解题思路
用deque容器写了个大数加法，然后挨个插在链表中，可以说是相当low了。
## C++(67ms)
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        vector<int>r1,r2;
        while(l1!=NULL){r1.push_back(l1->val);l1=l1->next;}
        while(l2!=NULL){r2.push_back(l2->val);l2=l2->next;}
        deque<int> re;
        int flag=0;
        int i,j,t;
        for(i=r1.size()-1,j=r2.size()-1;i>=0&&j>=0;)
        {
                t=r1[i]+r2[j]+flag;
                flag=t/10;
                t=t%10;
                re.push_front(t);
                i--;
                j--;
        }
        while(i>=0){
            r1[i]+=flag;
            flag=r1[i]/10;
            r1[i]=r1[i]%10;
            re.push_front(r1[i]);
            i--;
        }
        while(j>=0){
            r2[j]+=flag;
            flag=r2[j]/10;
            r2[j]=r2[j]%10;
            re.push_front(r2[j]);
            j--;
        }
        if(flag)re.push_front(flag);
        ListNode *head=new ListNode(0);
        ListNode *ans;
        ans=head;
        i=0;
        for(;i<re.size()-1;i++)
        {
            head->val=re[i];
            head->next=new ListNode(0);
            head=head->next;
        }
        head->val=re[i];
        return ans;
    }
};
```
