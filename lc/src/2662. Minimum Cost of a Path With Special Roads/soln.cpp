#include <vector>
#include <queue>
#include <unordered_map>
#include <cmath>
#include <tuple>

using namespace std;

class Solution {
public:
    int minimumCost(vector<int>& start, vector<int>& target, vector<vector<int>>& specialRoads) {
        using T = tuple<int, int, int>; // cost, x, y
        priority_queue<T, vector<T>, greater<T>> heap;
        unordered_map<long long, int> visited;

        heap.emplace(0, start[0], start[1]);

        while (!heap.empty()) {
            auto [cost, x, y] = heap.top();
            heap.pop();

            long long key = (static_cast<long long>(x) << 32) | y;
            if (visited.count(key) && visited[key] <= cost)
                continue;

            visited[key] = cost;

            if (x == target[0] && y == target[1])
                return cost;

            int directCost = cost + abs(target[0] - x) + abs(target[1] - y);
            heap.emplace(directCost, target[0], target[1]);

            for (const auto& road : specialRoads) {
                int x1 = road[0], y1 = road[1];
                int x2 = road[2], y2 = road[3];
                int c  = road[4];

                int toStart = abs(x1 - x) + abs(y1 - y);
                int totalCost = cost + toStart + c;

                heap.emplace(totalCost, x2, y2);
            }
        }

        return -1; // unreachable
    }
};
