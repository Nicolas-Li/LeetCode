class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        import collections
        metric = collections.defaultdict(set)
        max_num = 0
        for route in routes:
            for i in route:
                if i > max_num:
                    max_num = i
                for j in route:
                    metric[i].add(j)
        import sys
        stop_num = max_num + 1
        dest = []
        rel = [0] * stop_num
        for l in range(len(routes) + 1):
            if l == 0:
                dest.append([S])
                rel[S] = 1
            else:
                lev = []
                for i in dest[l-1]:                    
                    for j in metric.get(i, []):
                        if rel[j] == 0:
                            rel[j] = 1
                            lev.append(j)
                dest.append(lev)
            if T in dest[l]:
                return l
        return -1