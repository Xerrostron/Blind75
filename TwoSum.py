class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #cant repeat number, 2 numbers will add up to target, ONE solution
        #index method wont work, because it returns first instance
        #need to use enumerate
        #first number is index, second number is value
        for numb, row in enumerate(nums):
            for number, col  in enumerate(nums):
                 if row + col == target:
                    if numb!= number:
                        return numb,number