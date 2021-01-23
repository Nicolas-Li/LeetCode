class Solution:
    def maxPower(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        last_c = None
        max_power = 0
        cur_power = 1
        for c in s:
            if last_c == c:
                cur_power += 1
            else:
                max_power = max_power if max_power > cur_power else cur_power
                cur_power = 1
            last_c = c
        return max_power if max_power > cur_power else cur_power
