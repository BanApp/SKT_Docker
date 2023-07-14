import random
import os

def generate_numbers(result_path):
    # Generate two random numbers
    number1 = random.randint(1, 1000)
    number2 = random.randint(1, 1000)

    # Save the numbers to input.txt
    input_file = os.path.join(result_path, 'input.txt')
    with open(input_file, 'w') as file:
        file.write(f"{number1} {number2}")

    return input_file

# Example usage
result_path = os.environ['RESULTPATH']
generate_numbers(result_path)
