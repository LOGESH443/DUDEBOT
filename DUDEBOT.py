import datetime
import pyqrcode
import png
from pyqrcode import QRCode

class DudeBot:
    def __init__(self, bot_name, birth_year):
        self.bot_name = bot_name
        self.birth_year = birth_year
        self.user_name = ""

    def greet(self):
        print(f"Hello! My name is {self.bot_name}.")
        print(f"I was created in {self.birth_year}.")

    def remind_name(self):
        print('Please, remind me your name.')
        self.user_name = input()
        print(f"What a great name you have, {self.user_name}!")

    def guess_age(self, y, m, d):
        today = datetime.datetime.now().date()
        dob = datetime.date(y, m, d)
        age = int((today - dob).days / 365.25)
        print(f"Your age is {age}; that's a good time to start programming!")

    def count(self):
        print('Now I will prove to you that I can count to any number you want.')
        num = int(input())
        for counter in range(num + 1):
            print(f"{counter} !")

    def calculate(self, a, b):
        print("Press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")
        option = int(input("Enter your option: "))
        if option == 1:
            result = a + b
            print("Addition: ", result)
        elif option == 2:
            result = a - b
            print("Subtraction: ", result)
        elif option == 3:
            result = a * b
            print("Multiplication: ", result)
        elif option == 4:
            if b != 0:
                result = a / b
                print("Division: ", result)
            else:
                print("Cannot divide by zero")
        else:
            print("Invalid Value")

    def generate_qrcode(self):
        s = input("Enter your website: ")
        url = pyqrcode.create(s)
        url.svg("myqr.svg", scale=10)
        url.png('myqr.png', scale=8)
        print("QR Code generated and saved as myqr.svg and myqr.png.")

    def end(self):
        print('Congratulations, have a nice day!')
        print('.................................')
        print('.................................')
        print('.................................')
        input()

bot = DudeBot('Dude', '2023')
bot.greet()
bot.remind_name()

while True:
    print("\nHow can I help you today?")
    print("1. Find my age")
    print("2. Count numbers")
    print("3. Solve a mathematical equation")
    print("4. Generate a QR code for my website")
    print("5. Exit")

    choice = int(input())
    if choice == 1:
        y = int(input("Enter the year: "))
        m = int(input("Enter the month: "))
        d = int(input("Enter the day: "))
        bot.guess_age(y, m, d)
    elif choice == 2:
        bot.count()
    elif choice == 3:
        a = int(input("Enter first value: "))
        b = int(input("Enter second value: "))
        bot.calculate(a, b)
    elif choice == 4:
        bot.generate_qrcode()
    elif choice == 5:
        bot.end()
        break
    else:
        print("Invalid choice. Please try again.")
