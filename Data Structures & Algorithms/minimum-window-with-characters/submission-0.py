class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        count = 0
        for ch in t:
            t_hash[ch] = 1 + t_hash.get(ch,0)
        i = j = start_index = 0
        required = len(t_hash)
        minlen = float("inf")

        while j < len(s):
            char = s[j]
            s_hash[char] = 1 + s_hash.get(char,0)

            if s_hash[char] == t_hash[char]:
                count += 1 

            while count == required:                       # was: if count == required (no shrink)
                if j - i + 1 < minlen:
                    minlen = j - i + 1
                    start_index = i

                left_char = s[i]
                if s_hash[left_char] > 0:
                    s_hash[left_char] -= 1
                    if left_char in t_hash and s_hash[left_char] < t_hash[left_char]:
                        count -= 1
                else:
                    del s_hash[left_char]

                i += 1

            j += 1

        return "" if minlen == float("inf") else s[start_index:start_index + minlen]