class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Fixed sliding window

        left = 0
        right = k - 1
        res = arr[left:right]
        count = 0
        sums = sum(res)
        while right < len(arr):
            sums += arr[right]
            
            if sums / k >= threshold:
                count += 1
            sums -= arr[left]
            left += 1
            right += 1
            
        return count