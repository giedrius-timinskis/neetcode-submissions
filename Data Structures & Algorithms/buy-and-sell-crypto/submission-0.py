import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = math.inf
        res = 0

        for i in range(len(prices)):
            n = prices[i]

            if n < min:
                min = n
                continue
            
            calc = n - min
            if calc > res:
                res = calc
            
        return res
        