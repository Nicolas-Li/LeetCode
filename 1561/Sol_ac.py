class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles.reverse()
        coins = 0
        for i in range(1, (len(piles) * 2 // 3) + 1, 2):
            coins += piles[i]
        return coins