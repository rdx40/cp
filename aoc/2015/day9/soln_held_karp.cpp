#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <climits>
#include <algorithm>

using namespace std;

using Graph = map<string, map<string, int>>;

// Reads the graph from a file
Graph build_graph_from_ip(const string& filename) {
    Graph graph;
    ifstream file(filename);
    string line;

    while (getline(file, line)) {
        istringstream iss(line);
        string city1, to, city2, eq;
        int distance;
        iss >> city1 >> to >> city2 >> eq >> distance;

        graph[city1][city2] = distance;
        graph[city2][city1] = distance; // undirected graph
    }

    return graph;
}

// Held-Karp TSP solution
int held_karp_shortest_route(const Graph& graph) {
    vector<string> cities;
    map<string, int> city_index;
    int index = 0;

    // Map cities to indices
    for (const auto& entry : graph) {
        cities.push_back(entry.first);
        city_index[entry.first] = index++;
    }

    int n = cities.size();
    vector<vector<int>> dp(1 << n, vector<int>(n, INT_MAX));

    // Initialize: cost to reach each city directly from "start"
    for (int i = 0; i < n; ++i) {
        dp[1 << i][i] = 0; // Cost of starting at city i is 0
    }

    // Fill DP table
    for (int mask = 0; mask < (1 << n); ++mask) {
        for (int u = 0; u < n; ++u) {
            if (!(mask & (1 << u))) continue;
            for (int v = 0; v < n; ++v) {
                if (mask & (1 << v)) continue; // already visited
                int next_mask = mask | (1 << v);
                int dist = graph.at(cities[u]).at(cities[v]);
                dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + dist);
            }
        }
    }

    // Get the minimum distance ending at any city
    int final_mask = (1 << n) - 1;
    int result = INT_MAX;
    for (int i = 0; i < n; ++i) {
        result = min(result, dp[final_mask][i]);
    }

    return result;
}

int main() {
    string filename = "input.txt";
    Graph graph = build_graph_from_ip(filename);
    cout << held_karp_shortest_route(graph) << endl;
    return 0;
}
//A More Efficient Solution — Dynamic Programming (Held-Karp Algorithm)
//The best-known exact solution for the Traveling Salesman Problem (TSP) uses Dynamic Programming + Bitmasking, known as the Held-Karp algorithm.
//


