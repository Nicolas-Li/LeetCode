class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if arr is None or len(arr) == 0:
            return 0
        elif len(arr) == 1:
            return 1
        max_len = 1
        cur_len = 1
        s = 0
        flag = True
        while flag and s < len(arr) - 1:
            if arr[s+1] != arr[s]:
                gt = True if arr[s+1] > arr[s] else False
                cur_len = 2
                for i in range(s+1, len(arr)-1):
                    if arr[i+1] != arr[i]:
                        if gt == (arr[i+1] < arr[i]):
                            gt = not gt
                            cur_len += 1
                            continue
                        else:
                            s = i
                    else:
                        s = i + 1
                    max_len = max(max_len, cur_len)
                    break
                else:
                    max_len = max(max_len, cur_len)
                    flag = False
            else:
                s += 1
        return max_len