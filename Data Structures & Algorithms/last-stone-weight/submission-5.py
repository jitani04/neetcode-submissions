class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        if len(stones) == 1:
            return stones[0] * -1
        while len(stones) > 1:
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1
            if y < x:
                heapq.heappush(stones, -(x - y))
        if not stones:
            return 0
        return -stones[0] if stones else 0