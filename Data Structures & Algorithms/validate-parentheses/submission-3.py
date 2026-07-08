class Solution:
    def isValid(self, s: str) -> bool:
        # naive pointers?
        # optimal stack - everytime you see a open bracket, push it into the stack
        # if you have a closed bracket, pop the stack and see if it matches 
        # if it does keep going, if it doesn't return false 

        stack = []

        for x in s: 
            if x == "(" or x == "{" or x == "[":
                stack.append(x)
            elif x == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()

            elif x == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()

            elif x == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()

        return len(stack) == 0
            