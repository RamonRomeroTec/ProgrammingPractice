import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        names = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday")
        return names[datetime.date(year,month,day).weekday()]
