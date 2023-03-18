class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                nums_rest = nums[i+1:]
                idx2 = i+1+nums_rest.index(target-nums[i])
                return [i, idx2]