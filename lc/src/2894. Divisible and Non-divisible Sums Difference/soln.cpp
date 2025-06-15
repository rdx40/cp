class Solution {
public:
    int sumOfDivisible(int n, int m){
        int cnt = n/m;
        return m*cnt*(cnt+1)/2;
    }
    int differenceOfSums(int n, int m) {
        int totalSum = n*(n+1)/2;
        int divSum = sumOfDivisible(n,m);
        int nondivSum = totalSum - divSum;
        return nondivSum - divSum;
    }
};


