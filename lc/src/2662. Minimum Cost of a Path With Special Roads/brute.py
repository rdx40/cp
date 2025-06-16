class Solution(object):
    def minimumCost(self, start, target, specialRoads):
        from collections import deque
        points = set()
        points.add(tuple(start))
        points.add(tuple(target))
        for x1, y1, x2, y2, _ in specialRoads:
            points.add((x1, y1))
            points.add((x2, y2))
        

        points = list(points)
        idx_map = {p: i for i, p in enumerate(points)}
        
        
        n = len(points)
        dist = [float('inf')] * n
        dist[idx_map[tuple(start)]] = 0
        
        
        for _ in range(n * 2):
            for i in range(n):
                x1, y1 = points[i]
                for j in range(n):
                    x2, y2 = points[j]
                    dist[j] = min(dist[j], dist[i] + abs(x1 - x2) + abs(y1 - y2))
            for x1, y1, x2, y2, cost in specialRoads:
                i = idx_map[(x1, y1)]
                j = idx_map[(x2, y2)]
                dist[j] = min(dist[j], dist[i] + cost)

        return dist[idx_map[tuple(target)]]
