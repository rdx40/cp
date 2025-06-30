class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> value = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
            {'C', 100}, {'D', 500}, {'M', 1000}
        };
        int total = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (i + 1 < s.length() && value[s[i]] < value[s[i + 1]])
                total -= value[s[i]];
            else
                total += value[s[i]];
        }
        return total;
    }
};

