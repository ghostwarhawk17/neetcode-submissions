class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied  = 0
        grumpy_score = 0
        max_window = 0
        l =0

        for r in range(len(customers)):
            if grumpy[r]:
                grumpy_score += customers[r]
            else:
                satisfied += customers[r]
            
            if (r - l + 1) > minutes:
                if grumpy[l]:
                    grumpy_score -= customers[l]
                l+=1

            max_window = max(max_window,grumpy_score)

        return satisfied + max_window

            
        