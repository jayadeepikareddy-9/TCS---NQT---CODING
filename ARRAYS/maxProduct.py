class Solution:
    def maxProduct(self, nums):
        res = nums[0]
        minProd = nums[0]
        maxProd = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr < 0:
                minProd, maxProd = maxProd, minProd
            maxProd = max(curr, maxProd*curr)
            minProd = min(curr, minProd*curr)
            res = max(res, maxProd)
        return res
    
nums = [2,3,-2,4]
sol = Solution()
print(sol.maxProduct(nums))


#2nd optimal solution

class Solution:
    def maxProduct(self,arr):
        n = len(arr)
        pre,suff = 1,1
        ans = float('-inf')
        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= arr[i]
            suff *= arr[n-i-1]
            ans = max(ans, pre, suff)
        return ans

arr = [10,2,-3,-10,-5,4,10]
sol = Solution()
print(sol.maxProduct(arr))