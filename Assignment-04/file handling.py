try:
    # File open in read mode
    with open('../sample.txt', 'r') as file:
        print("Reading file content:\n")  # Heading print

        # Line number tracking
        line_number = 1

        # File Read every line in file
        for line in file:
            # Output printing formate
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1

except FileNotFoundError:
    # if file not found then this output will show
    print("Error: The file 'sample.txt' was not found.")

