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
    int getDecimalValue(ListNode* head) {
        vector<int> digits;
        ListNode* current = head;
        while(current){
            digits.push_back(current->val);
            current = current->next;
        }
        int res = 0;
        for(int i=0; i<digits.size(); i++){
            if(digits.at(i)==1){res += pow(2, digits.size()-1-i);}
        }
        return res;
    }
};