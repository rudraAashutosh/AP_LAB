def display_first_and_last_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if lines:
                print("First line:", lines[0].strip())
                print("Last line:", lines[-1].strip())
            else:
                print("The file is empty.")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'LAB_01\\3\\output.txt'
display_first_and_last_line(file_path)