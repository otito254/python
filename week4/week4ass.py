def read_and_modify_file(input_file, output_file):
    # Try to open the input file and read its contents
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content as needed (e.g., convert to uppercase)
        modified_content = content.upper()

        # Open the output file and write the modified content to it
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content written to {output_file}")

    # Handle the case where the input file does not exist
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    
    # Handle any other exceptions that may occur
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
read_and_modify_file('input.txt', 'output.txt')

def handle_file_errors():
    # Prompt the user to enter a filename
    filename = input("Enter the filename: ")

    # Try to open the specified file and read its contents
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)

    # Handle the case where the file does not exist
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    
    # Handle the case where the file cannot be read due to permission issues
    except PermissionError:
        print(f"The file {filename} cannot be read due to permission issues.")

    # Handle any other exceptions that may occur
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
handle_file_errors()
