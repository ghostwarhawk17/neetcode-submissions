class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        arrlen=len(nums)
        majority=0
        for n in nums:
            if n in hashmap:
                hashmap[n]+=1
            else:
                hashmap[n]=1
        for i,m in enumerate(nums):
            if hashmap[m] > arrlen // 2:
                majority=m
        return majority


        