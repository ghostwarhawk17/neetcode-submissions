class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp={}
        for n in nums:
            if n in mapp:
                mapp[n]+=1
            else:
                mapp[n]=1
            
            if mapp[n] > 1:
                return True
        return False
         