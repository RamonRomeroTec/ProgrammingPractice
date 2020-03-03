class Solution:
    def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]  
        tp= [ [1], [1,1]  ]
        for x in range(rowIndex-2+1):
            tp.append([1])
        for j in range(2,rowIndex+1):
            while True:
                tp[j].append(tp[j-1][len(tp[j])-1]+tp[j-1][len(tp[j])])
                if len(tp[j])==j:
                    tp[j].append(1)
                    break
        return tp[-1]
                
        
        