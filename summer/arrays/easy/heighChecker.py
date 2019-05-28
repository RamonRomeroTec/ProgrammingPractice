#   Provar naive solution primero siempre
# # validar si alturas estan en orden

class Solution(object):
    def heightChecker(self, heights):
        aux = sorted(heights)
        c=0
        for i in range(len(heights)):
            if heights[i] != aux[i]:
                c=c+1
                
        return c
            