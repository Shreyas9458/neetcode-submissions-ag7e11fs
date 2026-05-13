class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = list()
        heapq.heapify_max(distances)

        for x, y in points:
            distance = (x ** 2 + y **2) ** 0.5
            if len(distances) == k:
                heapq.heappushpop_max(distances, (distance, [x, y]))
            else:
                heapq.heappush_max(distances, (distance, [x, y]))
        return [point for (d, point) in distances]
