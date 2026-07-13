class Solution:
    def reverse(self, x: int) -> int:
        string=str(abs(x))
        sign = -1 if x < 0 else 1
        reversed_int=int(string[::-1]) * sign

        if reversed_int > 2**31 -1 or reversed_int < -2**31:
            return 0
        return reversed_int
            
            

        