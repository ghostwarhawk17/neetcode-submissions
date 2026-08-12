from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l = 0
        longest = 0
        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:   # <-- must delete
                    del basket[fruits[l]]
                l += 1
            longest = max(longest, r - l + 1)
        return longest