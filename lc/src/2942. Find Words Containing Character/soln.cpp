class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> ans;
        for(int i=0;i<words.size();i++){
            if(words[i].find(x) != string::npos){ //or jus use -1 but npos usually used to indicate that item x is not found in the string
                ans.push_back(i);
            }
        }
        
        return ans;
    }
};
