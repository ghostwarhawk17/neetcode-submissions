class Solution:
    def maxScore(self, cardPoints: List[int], k: int):
        n = len(cardPoints)

        if k == n:
            return sum(cardPoints)

        window = n - k
        left = 0
        curr_sum = 0
        min_sum = float("inf")

        for right in range(n):
            curr_sum += cardPoints[right]
            if right - left + 1 > window:
                curr_sum -= cardPoints[left]
                left += 1
            if right - left + 1 == window:
                min_sum = min(min_sum, curr_sum)

        return sum(cardPoints) - min_sum