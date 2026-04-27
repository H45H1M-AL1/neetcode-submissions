class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = j = 0
        while i < n:
            nums[j] = nums[i]
            while i < n and nums[i] == nums[j]:
                i += 1
            j += 1
        return j
    
        