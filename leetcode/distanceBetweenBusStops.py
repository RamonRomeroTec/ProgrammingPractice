class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        if start>destination:
            start, destination = destination, start
        ta = destination
        tb = len(distance) + ta
        start = len(distance)+start
        distance=distance+distance
        return min(sum(distance[start:tb]),sum(distance[ta:start]))
            

