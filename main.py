import unittest
from datetime import datetime

def sum(a, b):
    return a + b

class SumTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 5)

class Greeter:
    @staticmethod
    def greet(name):
        
        trimmed_name = name.strip()

       
        capitalized_name = trimmed_name.capitalize()

        
        current_hour = datetime.now().hour

        # Saludo por defecto
        greeting = "Hello"

        # Determina el saludo adicional según la hora del día
        if 6 <= current_hour < 12:
            greeting += " Good morning"
        elif 18 <= current_hour < 22:
            greeting += " Good evening"
        else:
            greeting += " Good night"

       
        return f"{greeting} {capitalized_name}"

class GreeterTest(unittest.TestCase):
    def test_greet_morning(self):
        greeter = Greeter()
        self.assertIn(greeter.greet("Jorge"), ["Hello Good morning Jorge", "Hello Good morning Jorge"])

    def test_greet_evening(self):
        greeter = Greeter()
        self.assertIn(greeter.greet("Juana"), ["Hello Good evening Juana", "Hello Good evening Juana"])

    def test_greet_night(self):
        greeter = Greeter()
        self.assertIn(greeter.greet("Doe"), ["Hello Good night Doe", "Hello Good night Doe"])

if __name__ == '__main__':
    unittest.main()
