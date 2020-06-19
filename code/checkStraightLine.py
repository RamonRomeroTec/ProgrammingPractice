class Solution(object):
    def checkStraightLine(self, coordinates):
        if len(coordinates)==2:
            return True
        i=0
        try:
            p=float(coordinates[i][1]-coordinates[i+1][1])/ (coordinates[i][0]-coordinates[i+1][0])
          
        except Exception as e:
            for i in range(2,len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
            return True
        y=coordinates[i][1]-(p*coordinates[i][0])
        for i in range(2,len(coordinates)):
            if (p*coordinates[i][0]+y !=coordinates[i][1]):
                return False
            
        return True
        