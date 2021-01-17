#!/usr/bin/python 

def reverse(x):
    """This function reverses String"""
    return x[::-1]

def convertToString(y):
    """This function converts number to String"""
    numberConvertedToString = str(y)
    return numberConvertedToString

def validate(value):
    """This function validates the values"""
    if not value.isdigit():
        return False
    if int(value)<0:
        return False
    return True

def reserseSum(line):
    """This function takes line as param and returns the reversed sum"""
    values = line.split(" ")

    #validate and reverse value in values, store values in array
    index = 0
    isValueValid = True
    for value in values:
        isValueValid = isValueValid and validate(value) 
        values[index] = reverse(value)
        index += 1
    
    #Skip if line is invalid
    if isValueValid == False or len(values) > 2:
        return -1

    #sum number
    sum=0
    for value in values:
        sum=sum + int(value)
    #resersed sum
    reversedSum=int(reverse(convertToString(sum)))
    return reversedSum

with open("inputs.txt", "r") as file_object:
    """Reads file, uses for loops, removes spaces at the beginning and end of string,
       skips line if it has invalid content, prints sum result"""
    lines = file_object.readlines()

    for line in lines:
        line=line.strip()
        
        sumResult = reserseSum(line)
        if sumResult == -1:
            #skip the invalid line
            print("Skipping invalid line: " + line)
            continue 

        print(sumResult)