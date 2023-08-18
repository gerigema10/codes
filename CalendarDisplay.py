import calendar

class CalendarDisplay:

    @staticmethod
    def display_monthly_calendar(year, month):
        cal = calendar.month(year, month)
        return cal

    @staticmethod
    def display_yearly_calendar(year):
        cal = calendar.calendar(year)
        return cal
