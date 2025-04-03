#longest consecutive sequence
#Runs in O(n)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        #Hash the array List[int] into a set

        num_set = set(nums)
        #0,2,3,1
        #Find an endpoint for this algorithm(it doesnt have anything lower than it)

        for num in num_set:
            #This a simple look-up since hashing, if nothing lower, the endpoint is One
            if num-1 not in num_set:
                length = 1
                #Simple look up, keeps maxing the length with compared hashed values 
                while num + length in num_set:
                    length +=1
                
                longest = max(longest,length)
        return longest