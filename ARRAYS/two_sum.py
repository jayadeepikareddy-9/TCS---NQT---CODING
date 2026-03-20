class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return(left+1, right+1)
            if s < target:
                left += 1
            else:
                right -= 1
print(Solution().twoSum([2,7,11,15], 9))