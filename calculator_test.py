import unittest
import os
from flask import Flask
from calculator import perform_calculation

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        @self.app.route('/calculate/<operator>', methods=['POST'])
        def calculate(operator):
            path = os.path.dirname(os.path.abspath(__file__))
            input_file = os.path.join(path, 'input.txt')
            try:
                with open(input_file, 'r') as file:
                    operand1, operand2 = map(int, file.read().split())

                    if operator == '+':
                        result = operand1 + operand2
                    elif operator == '-':
                        result = operand1 - operand2
                    elif operator == '*':
                        result = operand1 * operand2
                    elif operator == '%':
                        result = operand1 % operand2
                    else:
                        return 'Invalid operator'

                    return str(result)
            except FileNotFoundError:
                return 'Input file not found'
            except Exception as e:
                return str(e)

    def tearDown(self):
        # Delete the input.txt file after each test
        os.remove('input.txt')

    def test_addition(self):
        with open('input.txt', 'w') as file:
            file.write('3 5')

        response = self.client.post('/calculate/+', data={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '8')

    def test_subtraction(self):
        with open('input.txt', 'w') as file:
            file.write('10 4')

        response = self.client.post('/calculate/-', data={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '6')

    def test_multiplication(self):
        with open('input.txt', 'w') as file:
            file.write('6 7')

        response = self.client.post('/calculate/*', data={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '42')

    def test_division(self):
        with open('input.txt', 'w') as file:
            file.write('20 5')

        response = self.client.post('/calculate/%', data={})
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(float(response.data.decode()), 4)

    def test_invalid_operator(self):
        with open('input.txt', 'w') as file:
            file.write('2 3')

        response = self.client.post('/calculate/$', data={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Invalid operator')

if __name__ == '__main__':
    unittest.main()
