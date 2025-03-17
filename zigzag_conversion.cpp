class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.size()) return s;
        vector<string> subresults(numRows, "");
        string result = "";
        int row;
        for(int char_id=1; char_id <= s.size(); char_id++) {
            row = 0;
            char_id--;
            for(int i=0; i<numRows; i++) {
                if(char_id >= s.size()) break;
                subresults[row] += s[char_id];
                row++;
                char_id++;
            }
            row--;
            for(int i=0; i<numRows-2; i++) {
                if(char_id >= s.size()) break;
                row--;
                subresults[row] += s[char_id];
                char_id++;
            }
        }
        for(int i=0; i<numRows; i++) result += subresults[i];
        return result;
    }
};