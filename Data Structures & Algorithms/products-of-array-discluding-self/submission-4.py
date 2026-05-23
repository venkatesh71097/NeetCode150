class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Method 1: Brute force... O(n^2)
        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
        #     res[i] = prod
        # return res

        # Method 2: Division O(n)
        # prod = 1
        # num_zeros = 0
        # Step1 : Get the pdt of all nums, and the number of zeros. If #zeros is 2 or above, the entire array is 0
        # for n in nums:
        #     if n!=0:
        #         prod *= n
        #     else:
        #         num_zeros += 1
        # if num_zeros > 1:
        #     return [0] * len(nums)
        
        # # Get a dummy list and start traversing...
        # # If the number is valid, and there is # of zeros >= 1 or above...
        # # pdt of other numbers will turn that digit to 0. 
        # # If you hit the zero number, pdt is exactly the nonzero number product
        # # If #zeros = 0, then get the pdt and divide it by the exact number in the traversal
        # res = [0] * len(nums)
        # for i, n in enumerate(nums):
        #     if num_zeros:
        #         if n:
        #             res[i] = 0
        #         else:
        #             res[i] = prod
        #     else:
        #         res[i] = prod // n
        # return res

        # Method 3: Prefix suffix
        res = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * suffix
            suffix = suffix * nums[i]
        return res
        
        # prefix = [0] * len(nums)
        # suffix = [0] * len(nums)
        # res = [0] * len(nums)
        # prefix[0] = suffix[-1] = 1

        # for i in range(1, len(nums)):
        #     prefix[i] = nums[i-1] * prefix[i-1]

        # for i in range(len(nums)-2, -1, -1):
        #     suffix[i] = nums[i+1] * suffix[i+1]

        # for i in range(len(nums)):
        #     res[i] = prefix[i] * suffix[i]
        # return res