class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
        
        for char in s:
            if char == "(":
                self.stack.append(")")
            elif char == "{":
                self.stack.append("}")
            elif char == "[":
                self.stack.append("]")        
            else:
                if not self.stack or self.stack.pop() != char:
                    print(char)
                    return False
                
        return len(self.stack) == 0


solution = Solution()
print(solution.isValid("((({{{[[[]]]}}}))"))