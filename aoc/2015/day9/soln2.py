from itertools import permutations

def build_graph_from_ip(filename):
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            city1, city2 = parts[0], parts[2]
            distance = int(parts[4])

            graph.setdefault(city1, {})[city2] = distance
            graph.setdefault(city2, {})[city1] = distance
    return graph

def route_distance(route, graph):
    return sum(graph[route[i]][route[i+1]] for i in range(len(route) - 1))

def find_longest_route(graph):
    cities = list(graph.keys())
    all_routes = permutations(cities)
    return max(route_distance(route, graph) for route in all_routes)

graph = build_graph_from_ip('input.txt')
print(find_longest_route(graph))

