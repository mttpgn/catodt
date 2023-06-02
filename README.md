# catodt 
## ODT Document Utilities
This directory contains two Python scripts for managing ODT (Open Document Text) documents.

These scripts may be helpful for a writing project with chapters split into many distinct files.

### 1. Word Count (`word_count.py`) 
This script takes a directory path as a command line argument, and counts the number of words in each .odt file in the directory. It prints the word count for each file and the total word count for all files. 
#### Usage 
``` python3 word_count.py chapters/ ``` 

Replace `chapters/` with the path to the directory containing your .odt files. 

### 2. Document Concatenation (`concatenate_documents.py`) 
This script takes a directory path and an output file name as command line arguments, concatenates all .odt files in the directory into a single document, and saves the result as the specified output file. If the output file name ends with `.pdf`, the script also converts the concatenated document to PDF format. 
#### Usage 
``` python3 concatenate_documents.py chapters/ chapters_01-49.odt``` 

Replace `chapters/` with the path to the directory containing your .odt files, and `chapters_01-49.odt` with the name of the file you want to save the concatenated document as. If the last argument ends with `.pdf`, the concatenated document will be converted to PDF format. If the last argument ends with `.odt`, the concatenated document will be an ODT document. 

Regardless of output format, lines starting with the word "Chapter" will be promoted to a headers style.

ODT and PDF are currently the only two supported output formats. 

In both scripts, if no .odt files are found in the specified directory, the script will print an error message and exit. 

#### Note 
To run these scripts, you need to have the following Python libraries installed:
 - odfpy 
 - pypandoc 

You can install these libraries using pip: ``` python -m pip install odfpy pypandoc ```
