/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* swap(TreeNode* node) {
        TreeNode* currentnode = new TreeNode(node->val, node->right, node->left);
        if(currentnode->left) currentnode->left = swap(currentnode->left);
        if(currentnode->right) currentnode->right = swap(currentnode->right);
        return currentnode;
    }
    TreeNode* invertTree(TreeNode* root) {
        if(!root) return nullptr;
        return swap(root);
    }
};