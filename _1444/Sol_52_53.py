class Solution:
    def __init__(self):
        self.way_num = 0

    def normal(self, lis):
        start = 0
        end = len(lis)
        for i in range(len(lis)):
            if lis[i] == 0:
                start += 1
            else:
                break
        for i in range(len(lis) - 1, -1, -1):
            if lis[i] == 0:
                end -= 1
            else:
                break
        for i in range(start, end):
            lis[i] = 1

    def trim_str(self, pizza: List[str]) -> List[List[int]]:
        piz = []
        row_sum = []
        col_sum = [0] * len(pizza[0])
        for r in pizza:
            row = []
            r_sum = 0
            for i, c in enumerate(r):
                cur = 1 if c == "A" else 0
                col_sum[i] += cur
                r_sum += cur
                row.append(cur)
            row_sum.append(r_sum)
            piz.append(row)
        self.normal(row_sum)
        self.normal(col_sum)
        ret = []
        for i in range(len(row_sum)):
            if row_sum[i] > 0:
                row = []
                for j in range(len(col_sum)):
                    if col_sum[j] > 0:
                        row.append(piz[i][j])
                ret.append(row)
        return ret

    def trim(self, pizza: List[List[int]]) -> List[List[int]]:
        row_sum = []
        col_sum = [0] * len(pizza[0])
        for r in pizza:
            row = []
            r_sum = 0
            for i, c in enumerate(r):
                col_sum[i] += c
                r_sum += c
                row.append(c)
            row_sum.append(r_sum)
        self.normal(row_sum)
        self.normal(col_sum)
        ret = []
        for i in range(len(row_sum)):
            if row_sum[i] > 0:
                row = []
                for j in range(len(col_sum)):
                    if col_sum[j] > 0:
                        row.append(pizza[i][j])
                ret.append(row)
        return ret
    
    def cut(self, i, j, pizza: List[List[int]]) -> List[List[int]]:
        if j is None:
            return any (1 in row for row in pizza[0:i+1]), pizza[i+1:]
        if i is None:
            return any (1 in row for row in [row[0:j+1] for row in pizza]), [row[j+1:] for row in pizza]
    
    def dfs(self, pizza: List[List[int]], k: int) -> int:
        # print(k)
        if k == 1:
            # print(pizza)
            return 1 if any (1 in row for row in pizza) else 0
        else:
            pizza_copy = self.trim(pizza)
            # print(pizza_copy)
            m = len(pizza_copy)
            if m == 0:
                return 0
            n = len(pizza_copy[0])
            if m + n <= k:
                return 0
            ret = 0
            # 按行切割
            for i in range(m-1):       
                flag, pizza_cut = self.cut(i, None, pizza_copy)  
                if flag:       
                    ret += self.dfs(pizza_cut, k-1)
            # 按列切割
            for j in range(n-1):      
                flag, pizza_cut = self.cut(None, j, pizza_copy)  
                if flag:                    
                    ret += self.dfs(pizza_cut, k-1)
            return ret % 1000000007


    def ways(self, pizza: List[str], k: int) -> int:
        pizza = self.trim_str(pizza)
        m = len(pizza)
        n = len(pizza[0])
        if m + n <= k:
            return 0
        return self.dfs(pizza, k)
        
        