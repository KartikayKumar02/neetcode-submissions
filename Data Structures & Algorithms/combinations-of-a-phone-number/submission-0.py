class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def dfs(index,path):
            if len(digits) == index:
                result.append(path)
                return
            
            current_digit = digits[index]
            for letter in hashmap[current_digit]:
                
                # 4. THE LEAP OF FAITH: Pick the letter, and move to the next digit
                dfs(index + 1, path + letter)

        # Start at the 0th digit, with an empty string
        dfs(0, "")
        return result


            
        
        