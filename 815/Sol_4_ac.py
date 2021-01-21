class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        route_sets = collections.defaultdict(set)
        bus_num = len(routes) + 2
        metric = [[-1] * bus_num for _ in range(bus_num)]
        bus_i = 1
        for route in routes:
            if S in route:
                metric[0][bus_i] = 1
                metric[bus_i][0] = 1
            if T in route:
                metric[bus_i][bus_num - 1] = 0
                metric[bus_num - 1][bus_i] = 0
            route_sets[bus_i] = set(route)
            bus_i += 1
        for i in range(1, bus_num - 1):
            for j in range(i + 1, bus_num - 1):
                if len(route_sets[i].intersection(route_sets[j])) > 0:
                    metric[i][j] = 1
                    metric[j][i] = 1
        for i in range(bus_num):
            metric[i][i] = 0
            
        fid = 0
        tid = bus_num - 1
        import sys
        key = [sys.maxsize] * bus_num
        key[fid] = 0
        rel = [fid]
        min_v = fid
        while len(rel) <= bus_num and min_v != tid:
            for i in range(bus_num):
                if i != min_v and i not in rel and \
                    metric[min_v][i] >= 0 and \
                    key[i] > key[min_v] + metric[min_v][i]:
                    key[i] = key[min_v] + metric[min_v][i]
            if min_v not in rel:
                rel.append(min_v)
            min_v = tid
            for i in range(bus_num):
                if i not in rel and key[i] < key[min_v]:
                    min_v = i
        return -1 if key[tid] == sys.maxsize else key[tid]
