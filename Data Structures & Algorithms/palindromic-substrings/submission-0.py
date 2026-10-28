class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0
        for i in range(len(s)):
            # odd length
                l = r = i
                curr_count  = 0
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    curr_count += 1
                    r += 1
                    l -=1
                total_count += curr_count
                l = i
                r = i + 1
                curr_count = 0
                while l>=0 and r < len(s) and s[l] == s[r]:
                    curr_count += 1
                    r +=1
                    l-=1
                total_count += curr_count
        return total_count