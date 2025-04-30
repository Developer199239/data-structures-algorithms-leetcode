class Solution(object):
    def isVowel(self, s):
        if s.upper() == "A" or s.upper() == "E" or s.upper() == "I" or s.upper() == "O" or s.upper() == "U":
            return True
        return False
    
    def reverseVowels(self, s):
        s = list(s)
        start = 0
        end = len(s) - 1

        while start < end:
            isStartVowel = self.isVowel(s[start]) 
            isEndVowel = self.isVowel(s[end])
            if isStartVowel and isEndVowel: 
                s[start],s[end] = s[end], s[start]
                start +=1
                end -=1
            elif isStartVowel and not isEndVowel:
                  end -=1
            elif not isStartVowel and isEndVowel:
                start +=1
            else:
               start +=1
               end -=1   

        return ''.join(s)            

        
obj = Solution()
print(obj.reverseVowels("IceCreAm"))

# https://leetcode.com/problems/reverse-vowels-of-a-string/
