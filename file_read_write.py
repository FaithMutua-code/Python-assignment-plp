def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        # Try to open the file for reading
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Could not read the file. Please check the file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
