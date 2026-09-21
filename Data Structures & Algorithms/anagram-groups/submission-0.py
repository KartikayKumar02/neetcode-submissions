class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = collections.defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in freq:
                freq[sorted_word].append(word)
            else:
                freq[sorted_word] = [word]
        
        return list(freq.values())




        