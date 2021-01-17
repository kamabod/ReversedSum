# ReversedSum

Author: Kamila Bodurka

# Python Coding Assigment
This is a Python program which can rapidly reverse numbers and output their reversed sum.

## Overview of Functionality
This application is capable of reading an input file, reversing the input numbers and calculating their reversed sum.

## Project Design and Implementation
This application consists of Main file, Input File and UnitTest File and ReadMe File.

### Input File
The first line of the input file contains only one positive integer. The following cases contain mostly two numbers separated by space. Some other cases contain 3 numbers, symbols, letters, lines that are empty, lines with excessive spaces or negative numbers. For each line, the program prints one line containing only one integer which is a reversed sum of two reversed integers. The leading zeros are omitted in the output.
If a line contains an error, it is skipped and a message is displayed that the program is:"Skipping invalid line:" and the line contents is displayed.

### Main
Main has 4 funtions used to convert number to String , reverse the number, validate the number and reverse the sum.
Validations check if a string has digits, is numbers are positive, if there are only 2 numbers in the line.
Main is also able to read the input file. It uses for loops, removes spaces at the beginning and end of string. 
If a line has invalid content, it is skipped and a message is displayed informing the user about it.

### UnitTest
UnitTest imports the unitTest module and tests 3 functions from the main. It tests reverse method, convertToString method and reverseSum method. To test the reverseSum method parameterized test case is used. 

## Test Cases Are Covering the Scenarios:
- empty lines
- symbols and letters instead of numbers
- excessive spaces
- more than two numbers
- negative numbers

## Usage of Application

To run the application sucessfully there must be an input file present `input.txt` which is provided with the source code.
The main is run and the output is visible on the console.
The output includes one integer which is a reversed sum of 2 reversed integers provided in the input file.
```sh
python main.py
```