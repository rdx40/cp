class Solution {
public:
    bool isUgly(int n) {
        int nos[3] = {2, 3, 5};
        if (n<=0)
            return false;
        for (int i=0;i<=2;i++){
            while(n%nos[i] == 0){
                n = (int)(n/nos[i]);
            }
        }
        return n==1;        
    }
};
