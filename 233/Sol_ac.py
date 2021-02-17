class Solution:
    def __init__(self):
        self.dic = {
            0: 0,
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 1
        }
        for i in range(1, 10):
            key = eval('9' * i)
            val = i * (10 ** (i-1))
            self.dic[key] = val

    def countDigitOne(self, n: int) -> int:
        def dfs(s: int, e: int):
            if s == 0:
                if e in self.dic.keys():
                    return self.dic[e]
                else:
                    mid = eval('9' * (len(str(e)) - 1))
                    return dfs(0, mid) + dfs(mid + 1, e)                    
            else:
                s_str = str(s)
                e_str = str(e)
                if e_str[0] == '1':
                    return (e - s + 1) + dfs(int(s_str[1:]), int(e_str[1:]))
                else:
                    base = dfs(0, eval('9' * (len(s_str)-1)))
                    return base * (int(e_str[0])-1) + 10**(len(s_str)-1) + dfs(0, int(e_str[1:]))
        return dfs(0, n)

