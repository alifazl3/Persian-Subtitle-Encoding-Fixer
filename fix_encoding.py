# coding: utf-8
import codecs
import os
import sys

# Get input directory and possibly output directory
if len(sys.argv) >= 2:
    input_directory = sys.argv[1]
else:
    input_directory = input("Please enter the input directory: ")

if len(sys.argv) == 3:
    output_directory = sys.argv[2]
else:
    # Create an output directory named 'fix_' + input_directory
    output_directory = 'fix_' + os.path.basename(os.path.normpath(input_directory))

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop over all files in the input directory
for filename in os.listdir(input_directory):
    # Only process .srt files
    if filename.endswith('.srt'):
        input_file_path = os.path.join(input_directory, filename)
        
        # Prepare the output file path
        output_file_path = os.path.join(output_directory, filename)
        
        try:
            # Open the input file with 'Windows-1256' encoding and read the content
            with codecs.open(input_file_path, 'r', encoding='windows-1256') as input_file:
                text = input_file.read()

            # Open the output file in write mode with 'utf-8' encoding and write the content
            with codecs.open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(text)
                
            print(f'Successfully converted {filename}.')

        except Exception as e:
            print(f'An error occurred while converting {filename}: {str(e)}')

