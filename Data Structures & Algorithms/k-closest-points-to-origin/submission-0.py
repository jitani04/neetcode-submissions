class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x1, y1 in points:
            euc_d = x1** 2 + y1 ** 2
            distances.append([euc_d, x1, y1])

        heapq.heapify(distances)
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(distances)
            res.append([x,y])
            k -= 1

        return res