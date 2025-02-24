class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            # First, compute the squared distance for each point
            distances = []
            for point in points:
                dist = self.distance_squared(point)
                distances.append((point, dist))
            
            # Sort the points based on the squared distance (ascending order)
            distances.sort(key=lambda x: x[1])
            
            # Extract and return the k closest points
            return [point for point, _ in distances[:k]]

    
    def distance_squared(self, point: List[int]) -> int:
        return point[0]**2 + point[1]**2


class SolutionOptimized:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heappush(minHeap, (distance, point))
        
        return [heappop(minHeap)[1] for _ in range(k)]
