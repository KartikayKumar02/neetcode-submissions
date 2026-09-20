class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}


        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            if i in cache:
                return cache[i]
            

            # decode a single character:
            ways = dfs(i + 1)

            # decode 2 characters if valid

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in '0123456'):
                ways += dfs(i+2)
            
            cache[i] = ways
            return ways
        return dfs(0)