class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        # 我们将每一条公交路线（而不是每一个车站）看成图中的一个点，
        # 如果两条公交路线有交集，那么它们在图中对应的点之间就有一条边。
        # 此外，起点站 S 和终点站 T 也分别是图中的一个点，
        # 如果一条公交路线包含了 S 或 T，那么也需要和 S 或 T 对应的点连一条边。
        # 此时，在这个图上从 S 到 T 的最短路径长度即为答案，
        # 我们可以用广度优先搜索来找出最短路径。

        # 在计算两条公交路线是否有交集时，可以用的方法有很多种。
        # 例如将公交路线放在集合中，检查两个集合的交集是否为空；
        # 或者将公交路线中的车站进行递增排序，并使用双指针的方法检查是否有相同的车站。

        if S == T: return 0
        routes = map(set, routes) # python2 的写法
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in xrange(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route: seen.add(node)
            if T in route: targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/bus-routes/solution/gong-jiao-lu-xian-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。