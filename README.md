# Persian Subtitle Encoding Fixer

This script converts the encoding of Persian subtitle (.srt) files from 'Windows-1256' to 'UTF-8'. It takes an input directory and optionally an output directory as command-line arguments, processes all .srt files in the input directory, and saves the converted files in the output directory. If an output directory is not provided, the script will create a new one named 'fix_' followed by the name of the input directory.

## Prerequisites

- Python 3

## How to Use

1. Save the script in a `.py` file, for example `fix_encoding.py`.

2. Open a terminal window and navigate to the directory where you saved the script.

3. Run the script with Python, providing the input directory and optionally the output directory:

```bash
python3 fix_encoding.py <input_directory> <output_directory>
```


Replace `<input_directory>` and `<output_directory>` with the paths to your actual directories. If you don't provide an output directory, the script will create a new one named 'fix_' followed by the name of the input directory. The script will convert all .srt files in the input directory and save the converted files in the output directory. The original files will not be modified.

## Note

This script assumes that the input files are in 'Windows-1256' encoding. If they are in a different encoding, you'll need to change 'windows-1256' to the correct encoding in the `codecs.open()` call in the script.

Also, please always make a backup of your files before running any conversion scripts.


