class Solution:
    def zipCells(self, cells: List[int]) -> int:
        ret = 0
        for i in cells:
            ret += i
            ret <<= 1
        return ret
    
    def unzipCells(self, z: int, cells: List[int]):
        for i in range(len(cells)-1, -1, -1):
            z >>= 1
            cells[i] = z & 1

    def prisonAfterADay(self, cells: List[int]) -> List[int]:
        ret = []
        ret.append(0)
        for i in range(1, len(cells)-1):
            ret.append(1 if cells[i-1] == cells[i+1] else 0)
        ret.append(0)
        return ret

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        exist = [-1 for _ in range(1024)]
        ez = set()
        i = 0
        for _ in range(N):
            z = self.zipCells(cells)
            if exist[z] == -1:
                exist[z] = i
                i += 1
                cells = self.prisonAfterADay(cells)
            else:
                mod = i - exist[z]
                j = N % mod
                for k in range(len(exist)):
                    if exist[k] >= exist[z] and exist[k] % mod == j:
                        ret = cells.copy()
                        self.unzipCells(k, ret)
                        return ret
        return cells