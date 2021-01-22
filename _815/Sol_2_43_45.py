class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # meric 是用嵌套字典实现的邻接矩阵
        # 只要两个站位于同一条线路上，距离就是1（乘坐1辆公交可达）
        metric = {}
        max_num = 0
        for route in routes:
            for i in route:
                if i > max_num:
                    max_num = i
                for j in route:
                    if i != j:
                        mec = metric.get(i, {})
                        mec.update({j: 1})
                        metric.update({i: mec})
        import sys
        stop_num = max_num + 1
        for i in range(stop_num):
            mec = metric.get(i, {})
            mec.update({i: 0})
            metric.update({i: mec})
        # 算法2 BFS
        dest = []
        rel = [0] * stop_num
        for l in range(len(routes) + 1):
            if l == 0:
                dest.append([S])
                rel[S] = 1
            else:
                lev = []
                for i in dest[l-1]:                    
                    for j, cost in metric.get(i, {}).items():
                        if rel[j] == 0:
                            rel[j] = 1
                            if cost == 1:
                                lev.append(j)
                dest.append(lev)
            if T in dest[l]:
                return l
        return -1