from collections import deque
class RecentCounter:

    def __init__(self):
        self.a=deque([])
        

    def ping(self, t: int) -> int:
        self.a.append(t)
        l=self.a[-1]-3000
        while self.a[0] < l:
            self.a.popleft()
        return len(self.a)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)