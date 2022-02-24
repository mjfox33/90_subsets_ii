class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result_size = pow(2,n)
        result = []
        for i in range(result_size):
            current_set = []
            for j in range(n):
                if (i & (1<<j)) > 0:
                    current_set.append(nums[j])
            if not current_set in result:
                result.append(current_set)
        return result