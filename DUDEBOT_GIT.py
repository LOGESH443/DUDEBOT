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
        greeting = f"Hello! My name is {self.bot_name}.\nI was created in {self.birth_year}."
        print(greeting)
        return greeting

    def remind_name(self):
        print('Please, remind me your name.')
        self.user_name = input()
        print(f"What a great name you have, {self.user_name}!")
        return self.user_name

    def guess_age(self, y, m, d):
        today = datetime.datetime.now().date()
        dob = datetime.date(y, m, d)
        age = int((today - dob).days / 365.25)
        print(f"Your age is {age}; that's a good time to start programming!")
        return age

    def count(self, num):
        print('Now I will prove to you that I can count to any number you want.')
        for counter in range(num + 1):
            print(f"{counter} !")
        return list(range(num + 1))

    def calculate(self, a, b, option):
        print("Press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")
        result = None
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
                result = "Error"
        else:
            print("Invalid Value")
            result = "Invalid Value"
        return result

    def generate_qrcode(self, s):
        url = pyqrcode.create(s)
        url.svg("myqr.svg", scale=10)
        url.png('myqr.png', scale=8)
        print("QR Code generated and saved as myqr.svg and myqr.png.")
        return "QR Code generated"

    def end(self):
        message = 'Congratulations, have a nice day!'
        print(message)
        return message


