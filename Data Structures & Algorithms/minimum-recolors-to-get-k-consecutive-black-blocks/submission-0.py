class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0,0
        minop = float('inf')
        w_count = 0

        while right < len(blocks):
            if blocks[right] == 'W':
                w_count += 1 # 1, 2,
            
            while (right - left + 1) == k:
                minop = min(minop, w_count)
                if blocks[left] == 'W':
                    w_count -= 1
                left += 1
            right += 1
        return minop
