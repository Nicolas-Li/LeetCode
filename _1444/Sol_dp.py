#执行用时 :96 ms, 在所有 Python3 提交中击败了100.00%的用户
#内存消耗 :17.6 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def ways(self, pizza, k: int) -> int:
        module=int(1e9+7)
        rows,cols=len(pizza),len(pizza[0])
        # DP[remain][(row,col)]=dfs(row,col,remain)
        DP=[{(rows,cols):(0,0)} for i in range(k)] #初始值：空子pizza故怎么切都是0种！
        # _FA[r][c]=(FAR,_FAC) 表示以r行c列为左上角的子pizza，
        _FA=[[None]*cols for i in range(rows)]#从上往下第1个apple是FAR行，从左往右第1个apple是_FAC列。
        def FA(r,c): return (rows,cols) if r>=rows or c>=cols else _FA[r][c] #防止直接访问 _FA越界，做处理
        for r in range(rows)[::-1]:     #逆序递推！
            for c in range(cols)[::-1]:   #有apple：本坐标(r,c)；无apple：取右和下的行、列各自取小者。
                _FA[r][c] = (r,c) if 'A'==pizza[r][c] else tuple(map(min,zip(FA(r+1,c),FA(r,c+1)) ))
                if _FA[r][c]!=(rows,cols):
                    DP[0][_FA[r][c]] = (1,) # 子pizza[r:,c:]含有apple，切0刀算1种（要用元组，否则sum(..)会出错）
        # dfs(row,col,remain)=(across,vertical): 以row行col列为左上角的矩形子pizza，
        #切remain刀（首刀是横切有across种，首刀是竖切有vertical种，合计across+vertical种。
        def dfs(row,col,remain):    #★务必在代入之前用 规范为 (FAR,FAC)=FA(r,c)
            if (row, col) in DP[remain]: return DP[remain][row, col]  #查表（其中所有0种切法都已经赋值了）
            nr, nc = FA(row+1,col)  #求pizza[row+1:col:]的(FAR,FAC)
            across = (dfs(nr,nc,remain)[0]+(nr-row)*sum(dfs(nr,nc,remain-1)))%module
            nr, nc = FA(row,col+1)  #求pizza[row:col+1:]的(FAR,FAC)
            vertical= (dfs(nr,nc,remain)[1]+(nc-col)*sum(dfs(nr,nc,remain-1)))%module
            DP[remain][row, col]=(across,vertical)
            return (across,vertical)
        r0,c0=FA(0,0)
        return sum(dfs(r0,c0,k-1)) #调用dfs取横切+竖切之和

# 作者：java_Lee
# 链接：https://leetcode-cn.com/problems/number-of-ways-of-cutting-a-pizza/solution/ji-yi-hua-di-gui-bu-xu-yao-guan-dpci-xu-rong-yi-xi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。