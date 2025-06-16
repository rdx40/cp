import heapq

class Solution(object):
    def minimumCost(self, start, target, specialRoads):
        """
        :type start: List[int]
        :type target: List[int]
        :type specialRoads: List[List[int]]
        :rtype: int
        """
        heap = [(0, start[0], start[1])] #cost_rn, init x, init y
        visited = dict() # to avoid revisiting nodes with higher costs

        while heap:
            cost, x, y = heapq.heappop(heap) #pop locn with lowest accumulated cosr
            if (x, y) in visited and visited[(x, y)] <= cost:
                continue
            visited[(x, y)] = cost
            if (x, y) == (target[0], target[1]):
                return cost
            direct_cost = cost + abs(target[0] - x) + abs(target[1] - y)
            heapq.heappush(heap, (direct_cost, target[0], target[1]))
            for x1, y1, x2, y2, c in specialRoads:
                to_start_cost = abs(x1 - x) + abs(y1 - y)
                total_cost = cost + to_start_cost + c
                heapq.heappush(heap, (total_cost, x2, y2))
        return -1