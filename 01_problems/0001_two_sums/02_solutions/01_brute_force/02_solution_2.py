# 26/10/25           
# Runtime: 963ms, 31.15% 
# Memory: 18.52 MB, 72.29%

from typing import List 

# Idea: Compared to the first solution, we calculate the second number first, then find it 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_1 in range(len(nums)):
            num_to_find = target - nums[index_1]
            for index_2 in range(index_1 + 1, len(nums)): 
                if nums[index_2] == num_to_find: 
                    return [index_1, index_2]

# Comment: Just a small change, we reduce half of the runtime 