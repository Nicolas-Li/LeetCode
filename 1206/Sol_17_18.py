class Node:
    def __init__(self, val, right, down):
        self.val = val
        self.right = right
        self.down = down
    def __le__(self, other):
        return self.val <= other.val
    def __eq__(self, other):
        return self.val == other.val

class Skiplist:

    def __init__(self):
        self.level = 6
        self.skiplist = [[Node(0, None, None), Node(float("inf"), None, None)] for _ in range(self.level)]
        for lev in range(self.level):
            self.skiplist[lev][0].right = self.skiplist[lev][1]
            if lev < (self.level - 1):
                self.skiplist[lev][0].down = self.skiplist[lev + 1][0]
                self.skiplist[lev][1].down = self.skiplist[lev + 1][1]
    
    def random_level(self):
        prob = 2
        probs = [prob / 2 for _ in range(self.level)]
        probs.reverse()
        import random
        prob = random.random()
        for i, p in enumerate(probs):
            if prob < p:
                return i
        return self.level - 1
        

    def search(self, target: int) -> bool:
        node = self.skiplist[0][0]
        while node is not None:
            while node.right is not None:
                if node.right.val < target:
                    node = node.right
                elif node.right.val == target:
                    return True
                else:
                    break
            node = node.down
        return False
        

    def add(self, num: int) -> None:
        start_level = self.random_level()
        cur_level = 0
        pre_node = None
        node = self.skiplist[0][0]
        while node is not None:
            while node.right is not None:
                if node.right.val <= num:
                    node = node.right
                else:
                    if cur_level >= start_level:
                        new_node = Node(num, node.right, None)
                        if pre_node is not None:
                            pre_node.down = new_node
                        pre_node = new_node
                        node.right = new_node
                    break
            node = node.down
            cur_level += 1
        return False
        

    def erase(self, num: int) -> bool:
        flag = False
        node = self.skiplist[0][0]
        while node is not None:
            while node.right is not None:
                if node.right.val < num:
                    node = node.right
                else:
                    if node.right.val == num:
                        node.right = node.right.right
                        flag = True
                    break
            node = node.down
        return flag
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)