class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 0 -> false, 1 -> true
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1,-1,-1):
            curr_word = s[i]
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i + len(word)] == word :
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return True if dp[0] == 1 else False