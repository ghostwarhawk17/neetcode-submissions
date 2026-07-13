class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap={}
        result=[]
        for n in nums:
            if n not in hashmap:
                hashmap[n]=1
            else:
                hashmap[n]+=1
        for ele in hashmap:
            if hashmap[ele] > len(nums) / 3:
                result.append(ele)
        return result
        