class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # metric = [[-1 for i in range(stop_num)] for i in range(stop_num)]
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
        # 算法1 Dijstela
        # key列表代表S到每个点的最短路径
        key = [sys.maxsize] * stop_num
        key[S] = 0
        # rel列表代表已探索过的节点
        rel = [S]
        # min_v代表下一个探索的节点
        min_v = S
        while len(rel) <= stop_num and min_v != T:
            for i in range(stop_num):
                if i != min_v and i not in rel \
                    and metric.get(min_v, None) is not None \
                    and metric[min_v].get(i, None) is not None \
                    and key[i] > key[min_v] + metric[min_v][i]:
                    key[i] = key[min_v] + metric[min_v][i]
            if min_v not in rel:
                rel.append(min_v)
            min_v = T
            for i in range(stop_num):
                if i not in rel and key[i] < key[min_v]:
                    min_v = i
        return -1 if key[T] == sys.maxsize else key[T]