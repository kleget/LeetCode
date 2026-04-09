class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        data = str(s)
        data = data.split(" ")
        clean_data = [item for item in data if item]
        return len(clean_data[-1])

obj = Solution()
print(obj.lengthOfLastWord("   fly me   to   the moon  "))