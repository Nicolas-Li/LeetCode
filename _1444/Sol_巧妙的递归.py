class Solution:
    def ways(self, pizza: [str], k: int) -> int:
    	mod=pow(10,9)+7
    	m,n=len(pizza),len(pizza[0])

    	# 前缀和：pre[i][j]表示以(i,j)为左上角的矩形中苹果个数
    	pre=[[0]*(n+1) for _ in range(m+1)]
    	for i in range(m-1,-1,-1):
    		for j in range(n-1,-1,-1):
    			cur=1 if pizza[i][j]=='A' else 0
    			pre[i][j]=pre[i+1][j]+pre[i][j+1]-pre[i+1][j+1]+cur

    	@functools.lru_cache(None)
    	def f(x,y,k):
    		apples=pre[x][y]
    		if apples<k:return 0 #苹果不够
    		if k==1:return 1

    		cnt=0
    		# 一开始代码卡在这个地方，以为要找到两个都包含苹果的相邻行/列才能切
    		# 从上往下/从左往右，有苹果的行/列才能切
    		for i in range(x+1,m):
    			if pre[i][y]<apples:cnt+=f(i,y,k-1)
    		for j in range(y+1,n):
    			if pre[x][j]<apples:cnt+=f(x,j,k-1)
    		return cnt%mod
    	return f(0,0,k)%mod

# 作者：niu-meng
# 链接：https://leetcode-cn.com/problems/number-of-ways-of-cutting-a-pizza/solution/qian-zhui-he-ji-yi-hua-di-gui-dong-tai-g-68vk/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。