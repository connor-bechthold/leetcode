class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            elif len(stack) == 0:
                return False
            else:
                end = stack.pop()
                if not self.isSameBracketType(end, char):
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

    def isSameBracketType(self, front, end):
        total = front + end
        if total == '()' or total == '[]' or total == '{}':
            return True
        else: 
            return False
