class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Consider `nums` as unsorted...
        # Brute force:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # Route 1: Hash with double pass
        # seen = {}
        # for i, n in enumerate(nums):
        #     seen[n] = i
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in seen and seen[diff] != i: #seen[diff] != i prevents duplicate indices
        #         return [i, seen[diff]]
        # return []

        # Route 2: Hash with single pass
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen: #and diff != n: [use this condn. for preventing duplicate #s at index]
                return [seen[diff], i]
            seen[n] = i
        return []