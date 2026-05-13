class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if x == y:
                continue
            if x != y:
                newY = abs(y-x)
                heapq.heappush_max(stones, newY)
        return stones[0] if len(stones) > 0 else 0
        