class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        window = defaultdict(int)
        l = 0

        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        for n in s1:
            count[n] += 1
        res = False

        for r in range(len(s2)):
            window[s2[r]] += 1 
            if r - l + 1 > len_s1:
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l+=1

            if window == count and r - l + 1== len(s1):
                res =  True
        return res


