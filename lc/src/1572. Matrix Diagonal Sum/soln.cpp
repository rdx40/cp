class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int n = mat.size();
        int total = 0;

        for (int i = 0; i < n; ++i) {
            total += mat[i][i];
            total += mat[i][n - 1 - i];
        }
        if (n % 2 == 1) {
            total -= mat[n / 2][n / 2];
        }

        return total;
    }
};

