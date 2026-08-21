class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Number : Frequency
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        arr = []
        for num, freq in count.items():
            arr.append((freq, num))
        arr.sort()

        res = []
        for _ in range(k):
            res.append(arr.pop()[1])
        return res
    
        
            