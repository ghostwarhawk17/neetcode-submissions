class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1       
            else:
                r = mid            
        peak = l

        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            v = mountainArr.get(mid)
            if v == target: return mid
            if v < target: l = mid + 1
            else:          r = mid - 1

       
        l, r = peak + 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            v = mountainArr.get(mid)
            if v == target: return mid
            if v < target: r = mid - 1   
            else:          l = mid + 1

        return -1