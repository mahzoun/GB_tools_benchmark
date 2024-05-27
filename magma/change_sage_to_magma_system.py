import sys
import re

def increase_numbers_in_text(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = file.read()

        # Find all the numbers in the text using regular expression
        numbers = re.findall(r'x\d+', data)

        # Convert each number to an integer and increase it by one
        increased_numbers = ['Fxx.' + str(int(num[1:]) + 1) for num in numbers]

        # Replace the original numbers with the increased numbers in the text
        data = re.sub(r'\n', ',\n', data)
        modified_data = re.sub(r'x\d+', lambda match: increased_numbers.pop(0), data)
        # modified_data = re.sub(r'..$', '', modified_data)
        # modified_data = re.sub(r'^(.*)$', r'[\1];', modified_data)
        with open(output_file, 'w') as file:
            file.write(modified_data)

        print("File successfully modified and saved to", output_file)
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        increase_numbers_in_text(input_file_path, output_file_path)
