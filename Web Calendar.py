from UserInput import UserInput
from CalendarDisplay import CalendarDisplay

class CalendarApp:

    def __init__(self):
        self.display_choice, self.arg1, self.arg2, self.arg3 = UserInput.get_input()

    def display_calendar(self):
        if self.display_choice == 'M':
            cal = CalendarDisplay.display_monthly_calendar(self.arg3, self.arg2)
            print(f"Calendar for {self.arg3}-{self.arg2:02d}:\n{cal}")
        else:
            cal = CalendarDisplay.display_yearly_calendar(self.arg3)
            print(f"Calendar for the year {self.arg3}:\n{cal}")

if __name__ == "__main__":
    calendar_app = CalendarApp()
    calendar_app.display_calendar()
