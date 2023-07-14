from flask import Flask, request
import os

#깃허브 액션 테스트

app = Flask(__name__)

path = os.environ['RESULTPATH']

@app.route('/calculate/<operator>', methods=['POST'])
def perform_calculation(operator):
    try:
        with open(str(path) + 'input.txt', 'r') as file:
            operand1, operand2 = map(int, file.read().split())
            
            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand1 - operand2
            elif operator == '*':
                result = operand1 * operand2
            elif operator == '%':
                result = operand1 / operand2
            else:
                return 'Invalid operator'
            
            return str(result)
    except FileNotFoundError:
        return 'Input file not found'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
