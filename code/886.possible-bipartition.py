#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start
class Solution:
    '''
    染色法：
        和758如出一辙
        1. 首先要将不能放在一起的边存储下来，使用字典即可
        2. 然后采用一个list染色，没有染色的节点为0， 染红色为1，染蓝色为-1
        3. 在遍历过程中使用DFS/BFS将所有的可能染上色的节点染色，如果相撞则返回
        4. 使用如果染色则跳过的方式来避免重复计算
    '''
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        dislike = collections.defaultdict(list)
        for x in dislikes:
            dislike[x[0] - 1].append(x[1] - 1)
            dislike[x[1] - 1].append(x[0] - 1)
        
        color = [0 for i in range(N)]
        for i in range(N):
            if color[i] != 0: continue
            bfs = collections.deque()
            bfs.append(i)
            color[i] = 1
            while bfs:
                cur = bfs.popleft()
                for e in dislike[cur]:
                    if color[e] != 0:
                        if color[cur] == color[e]:
                            return False
                    else:
                        color[e] = -color[cur]
                        bfs.append(e)
        return True

# @lc code=end

