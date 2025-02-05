#include <string>
#include <cmath>
using std::string;

class Solution {
public:
    int lr = 0;
    int ud = 0;

    bool judgeCircle(string moves) {
        if (moves.size()%2 != 0) { return false; }
        for(int i=0; i < moves.size(); i++)
        {
            if (abs(lr) > moves.size()/2 || abs(ud) > moves.size()/2){ return false; }
            switch (moves[i])
            {
                case 'U':
                    ud++;
                    break;
                case 'D':
                    ud--;
                    break;
                case 'L':
                    lr--;
                    break;
                case 'R':
                    lr++;
                    break;
            }
        }
        return (lr == 0 && ud == 0);
    }
};