class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        res = nums[-1] - nums[0]
        left, right = 0, nums[-1] - nums[0]

        def isvalid(mid):
            ind, count = 0, 0
            while ind < len(nums) - 1:
                if abs(nums[ind] - nums[ind + 1]) <= mid:   
                    count += 1
                    ind += 2
                else:
                    ind += 1
                if count == p:
                    return True
            return False

        while left <= right:
            mid = (left + right) // 2                         
            if isvalid(mid):
                res = mid
                right = mid - 1                          
            else:
                left = mid + 1                              

        return res