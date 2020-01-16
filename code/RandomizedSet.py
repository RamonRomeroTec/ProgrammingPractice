import random
class RandomizedSet(object):
    def __init__(self):
        self.s=set()
    def insert(self, val):
        if val not in self.s:
            self.s.add(val)
            return True
        else:
            return False
    def remove(self, val):
        if val in self.s:
            self.s.remove(val)
            return True
        else:
            return False
    def getRandom(self):
        return list(self.s)[random.randint(0,len(self.s)-1)]
        

