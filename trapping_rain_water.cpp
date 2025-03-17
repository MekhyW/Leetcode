class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size() < 3) return 0;
        int trapped = 0;
        int left_wall = 0;
        int right_wall = height.size()-1;
        for(int curlevel=0; curlevel<100000; curlevel++) {
            for(; left_wall < height.size(); left_wall++){if(height[left_wall]>curlevel) break;}
            for(; right_wall > left_wall; right_wall--){if(height[right_wall]>curlevel) break;}
            if(left_wall >= height.size() || right_wall <= left_wall) return trapped;
            for(int curcolumn=left_wall; curcolumn < right_wall; curcolumn++){
                if(height[curcolumn] <= curlevel) trapped++;
            }
        }
        return trapped;
    }
};