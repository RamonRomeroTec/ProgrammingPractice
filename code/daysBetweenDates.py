from datetime import datetime
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        date1 = datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((date1 - date2).days)
        
    