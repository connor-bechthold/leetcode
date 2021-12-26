class Solution:
    def generateParenthesis(self, n: int, op = 0, cl = 0, combo = "", sol = []) -> List[str]:
        return self.solution(0, 0, "", [], n)

    def solution(self, op, cl, combo, sol, n):
        
        if op == n and cl == n:
            sol.append(combo)
            return
    
        if op < n:
            self.solution(op + 1, cl, combo + "(", sol, n)
        if cl < op:
            self.solution(op, cl + 1, combo + ")", sol, n)
            
        return sol
