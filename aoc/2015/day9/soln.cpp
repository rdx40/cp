#include <iostream> //io
#include <fstream> //file stram
#include <sstream> //string stream
#include <vector>
#include <map>
#include <climits>
#include <algorithm>

using namespace std;

using Graph = map<string, map<string, int>>; //graph as an alias for nested map

Graph build_graph_from_ip(const string& filename){
	Graph graph;
	ifstream file(filename); //open file
	string line; 

	while(getline(file, line)){ //for each line
		istringstream iss(line); //parse line
		string city1, to, city2, eq;
		int distance;
		iss >> city1 >> to >> city2 >> eq >> distance;

		graph[city1][city2] = distance;
		graph[city2][city1] = distance;
	}
	return graph;
}



int route_distance(const vector<string>& route, const Graph& graph){
	int tot = 0;
	for(size_t i = 0; i<route.size()-1 ; ++i){
		tot += graph.at(route[i]).at(route[i+1]);
	}
	return tot;
}

int find_shortest_route(Graph& graph) {
    vector<string> cities;
    for (const auto& entry : graph) {
        cities.push_back(entry.first);
    }

    int min_distance = INT_MAX;

    sort(cities.begin(), cities.end());
    do {
        int dist = route_distance(cities, graph);
        min_distance = min(min_distance, dist);
    } while (next_permutation(cities.begin(), cities.end()));

    return min_distance;
}


int main() {
    string filename = "input.txt";
    Graph graph = build_graph_from_ip(filename);
    cout << find_shortest_route(graph) << endl;
    return 0;
}

