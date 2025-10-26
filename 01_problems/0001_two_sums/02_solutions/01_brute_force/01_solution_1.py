# 26/10/25           
# Runtime: 1802ms, 13.02% 
# Memory: 18.52 MB, 72.29%

from typing import List 

# Idea: normal brute-force, nothing much to say 

class Solution: 
    def twoSum(
        self, 
        nums: List[int], 
        target: int
    ) -> List[int]: 
        for index_1 in range(len(nums)):
            for index_2 in range(index_1 + 1, len(nums)): 
                if nums[index_1] + nums[index_2] == target: 
                    return [index_1, index_2]

