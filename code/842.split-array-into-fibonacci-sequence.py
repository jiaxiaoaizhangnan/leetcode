#
# @lc app=leetcode id=842 lang=python3
#
# [842] Split Array into Fibonacci Sequence
#

# @lc code=start
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n = len(S)
        for i in range(1, 11):
            for j in range(1, 11):
                if i + j >= n:
                    break
                L = self.buildFibo(S, i, j)
                if L:
                    return L
        return []
    
    def buildFibo(self, s, i, j):
        a = s[:i]
        b = s[i:i+j]
        if a[0] == '0' and i > 1:
            return []
        if b[0] == '0' and j > 1:
            return []
        
        offset = i + j
        n = len(s)
        x, y = int(a), int(b)
        arr = [x, y]
        while offset < n:
            z = x + y
            if z > 2147483647:
                return []
            
            c = str(z)
            k = len(c)
            if offset + k > n or s[offset:offset+k] != c:
                return []
            offset += k
            arr.append(z)
            x, y = y, z
        return arr
            
# @lc code=end

