import re
import sys

def extract_variables(polynomial):
    # Regular expression to find all variables in the form of x<number>
    return set(re.findall(r'x\d+', polynomial))

def process_polynomial_file(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.readlines()

    all_variables = set()
    for line in content:
        all_variables.update(extract_variables(line))

    # Sort variables in natural order
    sorted_variables = sorted(all_variables, key=lambda x: int(x[1:]))
    try: 
        with open(output_file, 'w') as file:
            # Write the variables in the first line
            file.write(" ".join(sorted_variables) + '\n')
            file.write(f"{p} \n")
            # Write the original content
            file.writelines(content)
            print("File successfully modified and saved to", output_file)
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    p = 2
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        process_polynomial_file(input_file_path, output_file_path)
