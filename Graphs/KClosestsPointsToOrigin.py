class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=self.distance_squared)
        
        return points[:k]
    
    def distance_squared(self, point: List[int]) -> int:
        return point[0]**2 + point[1]**2
