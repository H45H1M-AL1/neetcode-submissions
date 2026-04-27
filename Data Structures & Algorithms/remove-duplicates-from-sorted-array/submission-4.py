class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        for i in range(0, len(nums)):
            unique.add(nums[i])
        nums[:len(unique)-1] = sorted(unique)
        return len(unique)
        
        