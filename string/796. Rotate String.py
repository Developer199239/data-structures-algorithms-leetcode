class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        s = s + s
        return goal in s

obj = Solution()
print(obj.rotateString("abcde", "cdeab"))
