class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        task = list(counter.values())
        heapq.heapify_max(task)

        timer = 0
        q = deque()

        while task or q:
            timer += 1

            if task:
                count = heapq.heappop_max(task) - 1
                if count != 0:
                    q.append((timer + n, count))
            if q and q[0][0] == timer:
                heapq.heappush_max(task, q.popleft()[1])
        return timer
        