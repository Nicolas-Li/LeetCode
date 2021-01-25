class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        def reduce_stack():
            if len(stack) >= 3:
                if stack[-1] == "#" and stack[-2] == "#" and stack[-3] != "#":
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append("#")
                    return True
            return False
        for c in preorder.split(","):
            stack.append(c)            
            while(reduce_stack()):
                pass
        return len(stack) == 1 and stack[0] == "#"