class Solution:
    def minOperations(self, logs: List[str]) -> int:
        state = 0
        for op in logs:
            if op == '../' and state != 0:
                state -=1
            elif op=='./' or (op == '../' and state == 0):
                pass
            else:
                state+=1  
        return state 
        