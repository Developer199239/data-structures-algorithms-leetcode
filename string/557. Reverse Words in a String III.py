class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        spliteWithEmptyString = s.split(" ")

        for i in range(len(spliteWithEmptyString)):
            spliteWithEmptyString[i] = spliteWithEmptyString[i][::-1]
            
        return " ".join(spliteWithEmptyString)

        
obj = Solution()
print(obj.reverseWords("Let's take LeetCode contest"))
