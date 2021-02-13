class Solution:
    def clumsy(self, N: int) -> int:        
        def frac(n):
            if n <= 3:
                return 1
            elif n == 4:
                return -2
            else:
                return n-(n-1)*(n-2)//(n-3) + frac(n-4)
        
        if N == 1:
            return 1
        elif N == 2:
            return 2
        elif N == 3:
            return 6
        else:
            return N*(N-1)//(N-2) + frac(N-3)
