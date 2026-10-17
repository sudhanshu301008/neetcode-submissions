class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = 0
        numset = set(nums)
        longest = 0 
        for n in numset:
            if n-1 not in numset:
                lenght = 0 
                while (n +lenght) in numset:
                    lenght +=1 
                    longest = max(lenght,longest)
        return longest





                


            
        