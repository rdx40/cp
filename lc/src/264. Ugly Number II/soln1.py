import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        ugly_numbers = [1]
        seen = set(ugly_numbers)
        heap = [1]
        primes = [2, 3, 5]

        for i in range(n):
            current_ugly = heapq.heappop(heap)
            for p in primes:
                new_ugly = current_ugly * p
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return current_ugly

