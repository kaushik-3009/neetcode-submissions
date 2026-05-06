class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for index in range(len(nums)-1):
        #     if nums[index] == nums[index+1]:
        #         return True
        # return False

        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False