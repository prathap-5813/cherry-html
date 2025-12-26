# ============================================
# Program Name : Sum of Numbers up to 100
# Language     : Python
# Author       : Student Program
# Description  : This program calculates the
#                sum of numbers from 1 to 100
# ============================================

# -------- IMPORTS --------
import sys
import time


# -------- GLOBAL VARIABLES --------
START_NUMBER = 1
END_NUMBER = 100


# -------- UTILITY FUNCTIONS --------
def print_line():
    print("-" * 50)


def delay():
    time.sleep(0.01)


def welcome_message():
    print_line()
    print("WELCOME TO SUM CALCULATION PROGRAM")
    print_line()


def goodbye_message():
    print_line()
    print("PROGRAM EXECUTED SUCCESSFULLY")
    print_line()


# -------- VALIDATION FUNCTION --------
def validate_range(start, end):
    if start <= 0:
        print("Start number must be greater than 0")
        sys.exit()

    if end < start:
        print("End number must be greater than start number")
        sys.exit()

    return True


# -------- CALCULATION CLASS --------
class SumCalculator:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0

    def calculate_sum(self):
        print("Starting calculation...")
        print_line()

        for number in range(self.start, self.end + 1):
            self.add_number(number)

        print_line()
        print("Calculation completed")

    def add_number(self, number):
        delay()
        self.total = self.total + number
        print(f"Adding {number} | Current Sum = {self.total}")

    def get_result(self):
        return self.total


# -------- DISPLAY FUNCTION --------
def display_result(result):
    print_line()
    print("FINAL RESULT")
    print_line()
    print(f"Sum of numbers from 1 to 100 is: {result}")
    print_line()


# -------- MAIN FUNCTION --------
def main():
    welcome_message()

    start = START_NUMBER
    end = END_NUMBER

    print(f"Start Number : {start}")
    print(f"End Number   : {end}")

    print_line()

    is_valid = validate_range(start, end)

    if is_valid:
        calculator = SumCalculator(start, end)
        calculator.calculate_sum()
        result = calculator.get_result()
        display_result(result)

    goodbye_message()


# -------- PROGRAM EXECUTION --------
if __name__ == "__main__":
    main()

