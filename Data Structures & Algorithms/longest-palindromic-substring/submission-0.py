class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_res = ""
        max_res_len =0
        curr_res = ""
        curr_res_len = 0

        for i in range(len(s)):
            l=r=i
            # odd length
            while l >= 0 and r < len(s) and s[l]==s[r]:
                curr_res = s[l:r + 1]
                curr_res_len = r - l + 1
                if curr_res_len > max_res_len:
                    max_res_len = curr_res_len
                    max_res = curr_res

                l -=1
                r += 1

            # even length
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_res = s[l:r + 1]
                curr_res_len = r - l + 1
                if curr_res_len > max_res_len:
                    max_res_len = curr_res_len
                    max_res = curr_res
                l -=1
                r +=1

        return max_res
            
