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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==nullptr){return head;}
        vector<ListNode*> nodes;
        ListNode* current = head;
        while(current->next != nullptr){
            nodes.push_back(current);
            current = current->next;
        }
        current->next = nodes[0];
        nodes.push_back(current);
        k = k % nodes.size();
        if(k==0){return head;}
        nodes[nodes.size()-k-1]->next = nullptr;
        return nodes[nodes.size()-k];
    }
};