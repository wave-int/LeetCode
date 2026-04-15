class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        profit = 0
        half = int(k / 2)
        pricetegy = []
        for i in range (len(prices)):
            pricetegy.append(prices[i] * strategy[i])
        profit = sum(pricetegy)
        dif = 0- sum(pricetegy[0: k]) + sum(prices[half: k])
        maxdif = dif
        for i in range (1, len(strategy) - k + 1):
            dif += pricetegy[i - 1]
            dif -= prices[i + half - 1]
            dif -= pricetegy[i + k - 1]
            dif += prices[i + k - 1]
            maxdif = max(maxdif, dif)             
        return max(profit, profit + maxdif)