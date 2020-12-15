class Solution:
    def interpret(self, command):
        i=0
        while i<len(command):
            if command[i] == 'G':
                s.append('G')
                i+=1
            elif command[i] == '(' and command[i+1] == ')':
                s.append('o')
                i+=2
            else:
                s.append('al')
                i+=4
        return "".join(s)
                
        