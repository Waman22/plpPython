def process_file():
    # Get input filename from user
    input_filename = input("Enter the name of the file to read: ")
    
    # Generate output filename by adding '_modified' before the extension
    if '.' in input_filename:
        base_name, extension = input_filename.rsplit('.', 1)
        output_filename = f"{base_name}_modified.{extension}"
    else:
        output_filename = f"{input_filename}_modified"

    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write modified content to new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"Success! Modified file has been saved as: {output_filename}")
        print("Changes made: Converted all text to uppercase")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {str(e)}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

# Run the program
if __name__ == "__main__":
    print("File Processing Program")
    print("----------------------")
    process_file()