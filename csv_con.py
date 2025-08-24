import re

def extract(input_file, output_file, pattern):
    try:
        en_no, sem_no = "", "" 
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            reader = infile.readlines()
            for i, line in enumerate(reader):
                if re.search(r"BT\d{2}[A-Z]{3}\d{3}", line):
                    en_no = line
                
                if re.search(r"(AUTUMN|SPRING|SUMMER)", line):
                    sem_no = line
                
                if re.search(pattern, line):
                    lines_to_save = reader[i:min(i + 4, len(reader))]
                    cleaned_lines = [l.rstrip('\n').strip() for l in lines_to_save]
                    outfile.write("\"" + en_no.rstrip('\n').strip() + "\",\"" + "\",\"".join(cleaned_lines) + "\",\"" + sem_no.rstrip('\n').strip() + "\"\n")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def remove_first_line(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
            lines = infile.readlines()
            if len(lines) > 1:
                outfile.writelines(lines[1:])
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



for i in range(592):
    input_filename = "P_"+ str(i+1) +".txt"
    output_filename = "extracted.txt"
    regex_pattern = r"[A-Z]{3}\d{3}" 
    
    extract(input_filename, output_filename, regex_pattern)
    remove_first_line("extracted.txt", "final.txt")
