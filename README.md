# PDF Comparison Python Code

## Overview

The Python code is designed to compare the content of PDF files between two specified folders. The program extracts the written content of the PDF files in both folders and computes a unique identifier, or hash, for each file based on the extracted content. These hashes are then compared between the two folders to determine if any files have the same content. If two files in both folders have the same hash, it can be concluded that they have the same written content. However, it should be noted that this method cannot detect differences in non-written content such as images or signatures. The program generates an Excel sheet with the comparison results to make it easier for the user to analyze and compare the files.

## Requirements

There are some requirements for using this program:

- The code uses Python, so the computer where the code is installed should have Python installed [(Install Python)](https://www.python.org/downloads/).
- The code uses some Python libraries that have to be installed using the command prompt. Follow these steps to install them (if you have not yet installed Python, the `pip` command will not work):
  - Open the command prompt
  - Copy and execute the following lines: 
    - `pip install pandas`
    - `pip install PyPDF2`  
- The program file should be located in the same directory as the two folders that contain the PDF files to be compared.
- Although the program can be executed anyway, there should be no copies of the same file on either of the folders. The program can be executed once in order to check if there are any copies. If the hash values of two files are the same, it can be determined that the written content on the PDFs is the same. However, it should be noted that the two PDFs are not guaranteed to be exactly the same by the program, as the full content of the PDF (such as images or signatures) is not being compared.

This program can be used on a Windows system only.

## Usage

To use this program, follow these steps:

- Place the program file in the same directory as the two folders containing the PDF files to be compared.
- Ensure that the two folders are named correctly.
- To ensure that you are in the same directory as the program file follow these steps:
  - Open the directory where the program file and the two folders are located
  - Type “cmd” in the address bar and then hit Enter.
  - Alternatively, if you are using Windows 11, you can use the right-click context menu on the folder to "Open in Terminal"
- Execute the Python file in a command prompt by typing `python pdf_comparison` into the command prompt and pressing Enter.
- Wait for the program to finish running. Once it is complete, an Excel sheet with the comparison results will be generated in the same directory as the program file. The output file is named "result.csv".

## Output File Creation

Once the code has finished running, the resulting Excel sheet is named `result.csv` and is located in the same directory as the program file.

## Credits

This program was created by Gabriel Escobar.