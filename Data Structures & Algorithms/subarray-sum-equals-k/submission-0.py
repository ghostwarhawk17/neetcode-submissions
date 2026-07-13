class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = 0
        hashmap = {}
        hashmap[0] = 1
        count = 0

        for i in range(len(nums)):
            presum += nums[i]
            remain = presum - k
            if remain in hashmap:
                count += hashmap[remain]
            if presum in hashmap:
                hashmap[presum] += 1
            else:
                hashmap[presum] = 1

        return count
