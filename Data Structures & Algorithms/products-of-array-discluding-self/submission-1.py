class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product1 = 1
        zero_count = 0

        # First pass: calculate product of non-zero numbers and count zeros
        for n in nums:
            if n != 0:
                product1 *= n
            else:
                zero_count += 1

        # Second pass: build result array based on zero count
        for n in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                result.append(product1 if n == 0 else 0)
            else:
                result.append(product1 // n)

        return result
