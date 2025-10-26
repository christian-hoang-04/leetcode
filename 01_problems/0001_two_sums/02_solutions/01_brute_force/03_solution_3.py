# 26/10/25           
# Runtime: 695ms, 31.64% 
# Memory: 18.36 MB, 87.23%

from typing import List 

# Idea: Compared to the second solution, we let Python find the index instead of iterate the list.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_1 in range(len(nums)):
            num_to_find = target - nums[index_1]
            try:
                index_2 = nums.index(num_to_find)
            except: # This is to handle the case that we cannot find the second index
                continue
            if index_2 != index_1: # This is important because we might be wrong in case like [3,1,2], result = 6 
                return [index_1, index_2]

# Comment: Small improvement in both runtime and bigger in memory 
# We should utilize the features in the original library xD  