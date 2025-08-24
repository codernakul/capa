def split_file_at_string(input_file, output_prefix, target_string):
    try:
        with open(input_file, 'r') as infile:
            content = ""
            file_count = 1
            for line in infile:
                content += line
                if target_string in line:
                    output_filename = f"{output_prefix}_{file_count}.txt"
                    with open(output_filename, 'w') as outfile:
                        outfile.write(content)
                    content = ""
                    file_count += 1
            if content:
                output_filename = f"{output_prefix}_{file_count}.txt"
                with open(output_filename, 'w') as outfile:
                    outfile.write(content)

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_filename = "mech.txt"
output_file_prefix = "P"
target_string = "VISVESVARAYA NATIONAL INSTITUTE OF TECHNOLOGY"

split_file_at_string(input_filename, output_file_prefix, target_string)