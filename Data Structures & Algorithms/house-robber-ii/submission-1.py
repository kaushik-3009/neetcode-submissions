class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp_left = [0]*(len(nums)+1)
        dp_right = [0]*len(nums)
        dp_left[0] = nums[0]
        dp_left[1] = max(nums[0], nums[1])
        
        reversed_nums = nums[::-1]
        dp_right[0] = (reversed_nums[0])
        dp_right[1] =  max(reversed_nums[0], reversed_nums[1])
        for i in range(2, len(nums)-1):
            dp_left[i] = max(dp_left[i-1], dp_left[i-2] + nums[i])

        for j in range(2, len(nums)-1):
            dp_right[j] = max(dp_right[j-1], dp_right[j-2] + reversed_nums[j])
            

        return max(max(dp_left), max(dp_right))
# (res[i] = res[i-1], res[i-2]+nums[i])