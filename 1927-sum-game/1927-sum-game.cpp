class Solution {
public:
    bool sumGame(string num) {
        int n = num.size();
        int rightknownsum = 0;
        int leftknownsum = 0;

        int leftqnmark = 0;
        int rightqnmark = 0;

        for(int i = 0; i < n ; i++){
            if(num[i] == '?'){
                if(i < n/2){
                    leftqnmark++;
                }else{
                    rightqnmark++;
                }
            }else{
                if(i < n/2){
                    leftknownsum += num[i] - '0';
                }else{
                    rightknownsum += num[i] - '0';
                }
            }
        }
        int totalqnmark = leftqnmark + rightqnmark;

        if(totalqnmark % 2 == 1){
            return true;
        }
        
        int Left = 2 * leftknownsum + 9 * leftqnmark;
        int right = 2 * rightknownsum + 9 * rightqnmark;

        if (Left == right){
            return false;
        }else{
            return true;
        }
        

        
    }
};