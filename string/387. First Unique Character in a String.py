class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}
        index = 0
        for c in s:
            if c in char_count:
                char_count[c] +=1
            else:
                char_count[c] = 1

        for index, c in enumerate(s):
            if char_count[c] == 1:
                return index      

        return -1

obj = Solution()
print(obj.firstUniqChar("loveleetcode"))
