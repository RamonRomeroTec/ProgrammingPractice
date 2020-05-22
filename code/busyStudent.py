class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        s=0
        for i in range(len(startTime)):
            if startTime[i]<=queryTime and queryTime<=endTime[i]:
                s+=1
        return s
        