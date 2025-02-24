/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        unsigned long long int depth1, depth2, n1, n2;
        string sum;
        depth1 = depth2 = n1 = n2 = 0;
        ListNode *current1, *current2;
        ListNode* reshead = new ListNode(0);
        current1 = l1;
        current2 = l2;
        while(current1 || current2){
            if(current1){
                n1 += current1->val * pow(10, depth1);
                current1 = current1->next;
                depth1++;
            }
            if(current2){
                n2 += current2->val * pow(10, depth2);
                current2 = current2->next;
                depth2++;
            }
        }
        if(n1+n2==0){return reshead;}
        sum = to_string(n1+n2);
        current1 = reshead;
        for(int i=log10(n1+n2); i>=0; i--){
            current1->val = sum[i] - '0';
            if(i==0){break;}
            current1->next = new ListNode(0);
            current1 = current1->next;
        }
        return reshead;
    }
};