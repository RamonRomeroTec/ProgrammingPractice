class CustomStack:
    
    def __init__(self, maxSize: int):
        self.mx=maxSize
        self.s=[]   
        
    def push(self, x: int) -> None:
        if len(self.s)<self.mx:
            self.s.append(x)
            
    def pop(self) -> int:
        if self.s:
            return self.s.pop()
        else:
            return -1
        
    def increment(self, k: int, val: int) -> None:
        try:
            for i in range(k):
                self.s[i]+=val
        except:
            pass

