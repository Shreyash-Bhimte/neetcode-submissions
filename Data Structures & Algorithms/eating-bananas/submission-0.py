from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            k = mid
            t_hours = 0
            for pile in piles:
                hours = ceil(pile / mid)
                t_hours = t_hours + hours
            if t_hours <=h:
                right = mid-1
            else:
                left = mid+1
                

        return left