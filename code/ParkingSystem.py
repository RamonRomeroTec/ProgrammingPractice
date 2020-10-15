class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.d=[big,medium,small]
        
    def addCar(self, carType: int) -> bool:
        if carType == 1: 
            if self.d[0]:
                self.d[0]-=1
                return True
            else:
                return False
                
        elif carType == 2: 
            if self.d[1]:
                self.d[1]-=1
                return True
            else:
                return False
        else:
            if self.d[2]:
                self.d[2]-=1
                return True
            else:
                return False
        
