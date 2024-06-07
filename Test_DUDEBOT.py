import pytest
from dudebot import DudeBot
from unittest.mock import patch

def test_greet():
    bot = DudeBot('Dude', '2023')
    assert bot.greet() == "Hello! My name is Dude.\nI was created in 2023."

def test_remind_name(monkeypatch):
    bot = DudeBot('Dude', '2023')
    monkeypatch.setattr('builtins.input', lambda: 'John')
    assert bot.remind_name() == 'John'

def test_guess_age():
    bot = DudeBot('Dude', '2023')
    age = bot.guess_age(2000, 1, 1)
    assert age == 24  # Adjust based on current date

def test_count():
    bot = DudeBot('Dude', '2023')
    result = bot.count(5)
    assert result == [0, 1, 2, 3, 4, 5]

def test_calculate_add():
    bot = DudeBot('Dude', '2023')
    result = bot.calculate(2, 3, 1)
    assert result == 5

def test_calculate_sub():
    bot = DudeBot('Dude', '2023')
    result = bot.calculate(5, 3, 2)
    assert result == 2

def test_calculate_mul():
    bot = DudeBot('Dude', '2023')
    result = bot.calculate(2, 3, 3)
    assert result == 6

def test_calculate_div():
    bot = DudeBot('Dude', '2023')
    result = bot.calculate(6, 3, 4)
    assert result == 2

def test_calculate_div_zero():
    bot = DudeBot('Dude', '2023')
    result = bot.calculate(6, 0, 4)
    assert result == "Error"

def test_generate_qrcode():
    bot = DudeBot('Dude', '2023')
    result = bot.generate_qrcode("http://example.com")
    assert result == "QR Code generated"

def test_end():
    bot = DudeBot('Dude', '2023')
    assert bot.end() == 'Congratulations, have a nice day!'
