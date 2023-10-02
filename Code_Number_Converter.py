#This one converts the Code into numbers for various variables

import numpy as np
import Code_Number

def Converted_Number(ini_string):
    
    variables = []
    for i in range(1, len(ini_string)):
        char = ini_string[i]
        variables.append(Code_Number.Convert_Code_Number(char))
    return variables
