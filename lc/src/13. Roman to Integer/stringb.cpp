class Solution {
public:
    int romanToInt(string s) {
        unordered_map<string, int> specials = {
            {"IV", 4}, {"IX", 9}, {"XL", 40},
            {"XC", 90}, {"CD", 400}, {"CM", 900}
        };
        unordered_map<char, int> roman = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
            {'C', 100}, {'D', 500}, {'M', 1000}
        };
        int total = 0;
        for (int i = 0; i < s.length(); ) {
            if (i + 1 < s.length() && specials.count(s.substr(i, 2))) {
                total += specials[s.substr(i, 2)];
                i += 2;
            } else {
                total += roman[s[i]];
                i++;
            }
        }
        return total;
    }
};

