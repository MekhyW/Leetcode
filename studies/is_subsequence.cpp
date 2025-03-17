#include <string>
using std::string;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (t.size()==0 && s.size()>0){return false;}

        int cur=0;
        for(int looking=0; looking<s.size(); looking++)
        {
            if(cur>=t.size()){return false;}
            for(; cur<t.size(); cur++)
            {
                if(s[looking]==t[cur]){
                    cur++;
                    break;
                }
                if(cur==t.size()-1){return false;}
            }
        }
        return true;
    }
};