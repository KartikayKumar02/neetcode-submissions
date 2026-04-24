class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0

        length = len(chars)

        while read < length:
            chars[write] = chars[read]
            write += 1
            consecutive = read + 1
            while consecutive < length and chars[read] == chars[consecutive]:
                consecutive += 1
            if consecutive - read > 1:
                for char in str(consecutive - read):
                    chars[write] = char
                    write += 1
            read = consecutive
        return write


        


        