# Contains Duplicate Attemp 10/19/2022

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l =  len(nums)
        if l < 2:
            return False
        nums.sort()
        for i in range(l-1):
           if nums[i] == nums[i+1]:
                return True
        return False