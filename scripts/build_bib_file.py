import os

# Define the directory to walk through
dir_path = '../citations'

# Define the output file
output_file = '../bibliography.bib'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    outfile.write('******************\n\nAUTOGENERATED: DO NOT MODIFY \n\n******************')
    # Walk through the directory
    for dirpath, dirnames, filenames in os.walk(dir_path):
        # For each file in the directory
        for filename in filenames:
            # If the file is a .bib file
            if filename.endswith('.bib'):
                # Construct the full file path
                filepath = os.path.join(dirpath, filename)
                # Open the .bib file in read mode
                with open(filepath, 'r') as infile:
                    # Write the contents of the .bib file to the output file
                    outfile.write(infile.read())
                    # Write a newline character to the output file
                    outfile.write('\n')