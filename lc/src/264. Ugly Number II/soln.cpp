class Solution {
public:
    int nthUglyNumber(int n) {
        std::priority_queue<long, std::vector<long>, std::greater<long>> minHeap;
        std::set<long> seen;

        minHeap.push(1);
        seen.insert(1);

        long ugly = 1;
        int count = 0;
        std::vector<int> primes = {2, 3, 5};

        while (count < n) {
            ugly = minHeap.top();
            minHeap.pop();
            count++;

            for (int prime : primes) {
                long next = ugly * prime;
                if (seen.find(next) == seen.end()) {
                    minHeap.push(next);
                    seen.insert(next);
                }
            }
        }

        return static_cast<int>(ugly);
    }
};

