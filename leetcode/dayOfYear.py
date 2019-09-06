class Solution(object):
    def dayOfYear(self, date):
        months=[31, None, 31, 30, 31, 30, 31, 31,30,31,30, 31]
        date=[ int(x) for x in date.split("-")]
        year, month, day = date[0], date[1], date[2]
        if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
            months[1]=29
        else:
            months[1]=28
        return day+sum(months[:month-1])
            
        