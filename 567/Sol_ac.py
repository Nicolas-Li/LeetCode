class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) >= len(s1):
            s1_freq = collections.defaultdict(int)
            s2_freq = collections.defaultdict(int)
            for c in s1:
                s1_freq[c] += 1
            for end in range(0, len(s1)):
                s2_freq[s2[end]] += 1
            if all(s1_freq[key] == s2_freq[key] for key in s1_freq.keys()):
                return True
            for end in range(len(s1), len(s2)):
                s2_freq[s2[end]] += 1
                s2_freq[s2[end-len(s1)]] -= 1
                if all(s1_freq[key] == s2_freq[key] for key in s1_freq.keys()):
                    return True
        return False