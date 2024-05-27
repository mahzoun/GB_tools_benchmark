import sys
import re

def increase_numbers_in_text(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = file.read()
            pattern = r'x(\d+)'
            # Replacement pattern to wrap digits in brackets
            replacement = r'x[\1]'
            # Perform the replacement
            result = re.sub(pattern, replacement, data)
            pattern = r'\n'

            # Replacement pattern to replace newline with comma and newline
            replacement = ',\n'

            # Perform the replacement
            result = re.sub(pattern, replacement, result)
        # Output the modified content to a new file or print it
            with open(output_file, 'w') as file:
                file.write(result)
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
