class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a = 0
        b = 0
        while piles:
            if piles[0] > piles[-1] and piles[0] > piles[1]:
                a += piles[0]
                piles.pop(0)
            else:
                a += piles[-1]
                piles.pop(-1)
        return a if a > b else b