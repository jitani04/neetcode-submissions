class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = Counter(nums)
       
        sorted_dict = dict(sorted(frequency.items(), key=lambda item: item[1]))
        sorted_list = list(sorted_dict.keys())
        
        most_freq = []
        # for i in range(len(sorted_list) - 1, len(sorted_list) - k - 1, -1):
        #     print(sorted_list[i])
        #     most_freq.append(sorted_list[i])

        most_freq = sorted_list[-k:] #replace for loop with list slicing. this means -kth index to the end
        return most_freq
