class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() < 3) return 0;
        int left_wall = 0;
        int right_wall = height.size() - 1;
        int leftMax = height[left_wall];
        int rightMax = height[right_wall];
        int trapped = 0;
        while (left_wall < right_wall) {
            if (leftMax < rightMax) {
                left_wall++;
                if (height[left_wall] < leftMax) trapped += leftMax - height[left_wall];
                else leftMax = height[left_wall];
            } else {
                right_wall--;
                if (height[right_wall] < rightMax) trapped += rightMax - height[right_wall];
                else rightMax = height[right_wall];
            }
        }
        return trapped;
    }
};