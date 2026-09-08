class Solution:
    def permutations(self,nums,ds,ans,freq):
        if len(ds) == len(nums):
            ans.append(ds.copy())
            return
        for i in range(len(nums)):
            if i not in freq:
                freq[i] = 1
                ds.append(nums[i])
                self.permutations(nums,ds,ans,freq)
                ds.pop()
                del freq[i]
        

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        ds = []
        freq = defaultdict(int)
        self.permutations(nums,ds,ans,freq)
        return ans