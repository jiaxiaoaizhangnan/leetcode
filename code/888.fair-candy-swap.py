#
# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#

# @lc code=start
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        s_A = sum(A)
        s_B = sum(B)
        
        mid = (s_A + s_B)//2
        b = set(B)
        for n in A:
            if mid + n - s_A in b: ## s_A - n + m = mid
                return [n, mid + n - s_A]
# @lc code=end

