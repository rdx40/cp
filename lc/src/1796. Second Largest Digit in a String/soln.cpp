class Solution {
public:
    int secondHighest(string s) {
        set<int> digits;

        for (char c: s){
            if(isdigit(c)){
                digits.insert(c - '0');
            }
        }

        if(digits.size() < 2){
            return -1;
        }

        //set to vec
        vector<int> vec(digits.begin(), digits.end());
        return vec[vec.size() - 2];
    }
};
