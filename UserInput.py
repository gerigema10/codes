class UserInput:

    @staticmethod
    def get_input():
        display_choice = input("Enter 'M' to display monthly calendar or 'Y' to display yearly calendar: ").upper()
        while display_choice not in ['M', 'Y']:
            print("Invalid choice. Please enter 'M' or 'Y'.")
            display_choice = input("Enter 'M' to display monthly calendar or 'Y' to display yearly calendar: ").upper()

        if display_choice == 'M':
            start_date = int(input("Enter the start date: "))
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year: "))
            return 'M', start_date, month, year
        else:
            year = int(input("Enter the year: "))
            return 'Y', 1, 1, year  # Default month and start_date to 1
