class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")}]":
                if not stack:
                    return False
                top = stack.pop()
                if i == ")" and top != "(":
                    return False
                elif i == "}" and top != "{":
                    return False
                elif i == "]" and top != "[":
                    return False

        return not stack


        
