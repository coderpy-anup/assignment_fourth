'''
Task 2: Write and Append Data to a File
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''
def write_to_file(filename):
    data = input("Enter text to write to the file: ")
    try:
        with open(filename, 'w') as file:
            file.write(data + '\n')
        print(f"Data written successfully to {filename}")
    except Exception as e:
        print(f"An error occurred while writing: {e}")

def append_to_file(filename):
    additional_data = input("Enter additional text to append to the file: ")
    try:
        with open(filename, 'a') as file:
            file.write(additional_data + '\n')
        print("Data successfully appended.")
    except Exception as e:
        print(f"An error occurred while appending: {e}")

def read_file(filename):
    print(f"\nFinal content of {filename}:\n")
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"An error occurred while reading: {e}")


if __name__ == "__main__":
    file_name = "output.txt"
    write_to_file(file_name)
    append_to_file(file_name)
    read_file(file_name)