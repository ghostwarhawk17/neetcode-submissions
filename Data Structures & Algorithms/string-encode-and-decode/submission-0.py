class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for n in strs:
            s+=str(len(n)) + '#' + n
        return s

    def decode(self, s: str) -> List[str]:
        decoded_str,i=[],0
        while i < len(s) - 1:
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            decoded_str.append(s[j + 1 : j + length + 1])
            i=j + length + 1
        return list(decoded_str)

