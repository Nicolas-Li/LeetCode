class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostKDistinct(A, K) - self.atMostKDistinct(A, K-1)
    
    def atMostKDistinct(self, A: List[int], K: int) -> int:
        length = len(A)
        freq = [0 for _ in range(length+1)]

        left = right = count = res = 0
        while right < length:
            if freq[A[right]] == 0:
                count += 1
            freq[A[right]] += 1
            right += 1
            while count > K:
                freq[A[left]] -= 1
                if freq[A[left]] == 0:
                    count -= 1
                left += 1
            res += right - left
        return res
            

            
