class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        def firstbs():
            l = 0
            r = len(nums) - 1
            while l<=r:
                mid = (l + r) // 2
                if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                    return mid
                if nums[mid] == target and nums[mid - 1] == target:
                    r = mid - 1
                    continue
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        def lastbs():
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != target):
                    return mid
                if nums[mid] == target and nums[mid + 1] == target:
                    l = mid + 1
                    continue
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        res[0] = firstbs()
        res[1] = lastbs()

        return res
        


