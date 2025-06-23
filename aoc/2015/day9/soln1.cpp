// $ cat soln.cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <climits>
#include <algorithm>

using namespace std;

using Graph = map<string, map<string, int>>;

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
        graph[city2][city1] = distance;
    }

    return graph;
}

int route_distance(const vector<string>& route, const Graph& graph) {
    int total = 0;
    for (size_t i = 0; i < route.size() - 1; ++i) {
        total += graph.at(route[i]).at(route[i + 1]);
    }
    return total;
}

int find_longest_route(Graph& graph) {
    vector<string> cities;
    for (const auto& entry : graph) {
        cities.push_back(entry.first);
    }

    int max_distance = INT_MIN;

    sort(cities.begin(), cities.end());
    do {
        int dist = route_distance(cities, graph);
        max_distance = max(max_distance, dist);
    } while (next_permutation(cities.begin(), cities.end()));

    return max_distance;
}

int main() {
    string filename = "input.txt";
    Graph graph = build_graph_from_ip(filename);
    cout << find_longest_route(graph) << endl;
    return 0;
}

