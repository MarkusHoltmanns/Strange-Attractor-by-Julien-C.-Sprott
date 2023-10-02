import numpy as np

def Convert_Code_Number(char):
    number = None
    if char == " ":
        number = -4.5
    if char == "!":
        number = -4.4
    if char == "\"":
        number = -4.5
    if char == "§":
        number = -4.3
    if char == "$":
        number = -4.2
    if char == "%":
        number = -4.1
    if char == "&":
        number = -4.0
    if char == "`":
        number = -3.9
    if char == "(":
        number = -3.8
    if char == ")":
        number = -3.7
    if char == "*":
        number = -3.6
    if char == "+":
        number = -3.4
    if char == ",":
        number = -3.3
    if char == "-":
        number = -3.2
    if char == ".":
        number = -3.1
    if char == "/":
        number = -3.0
    if char == "0":
        number = -2.9
    if char == "1":
        number = -2.8
    if char == "2":
        number = -2.7
    if char == "3":
        number = -2.6
    if char == "4":
        number = -2.5
    if char == "5":
        number = -2.4
    if char == "6":
        number = -2.3
    if char == "7":
        number = -2.2
    if char == "8":
        number = -2.1
    if char == "9":
        number = -2.0
    if char == ":":
        number = -1.9
    if char == ";":
        number = -1.8
    if char == "<":
        number = -1.7
    if char == "=":
        number = -1.6
    if char == ">":
        number = -1.5
    if char == "?":
        number = -1.4
    if char == "#":
        number = -1.3
    if char == "A":
        number = -1.2
    if char == "B":
        number = -1.1
    if char == "C":
        number = -1.0
    if char == "D":
        number = -0.9
    if char == "E":
        number = -0.8
    if char == "F":
        number = -0.7
    if char == "G":
        number = -0.6
    if char == "H":
        number = -0.5
    if char == "I":
        number = -0.4
    if char == "J":
        number = -0.3
    if char == "K":
        number = -0.2
    if char == "L":
        number = -0.1
    if char == "M":
        number = 0.0
    if char == "N":
        number = 0.1
    if char == "O":
        number = 0.2
    if char == "P":
        number = 0.3
    if char == "Q":
        number = 0.4
    if char == "R":
        number = 0.5
    if char == "S":
        number = 0.6
    if char == "T":
        number = 0.7
    if char == "U":
        number = 0.8
    if char == "V":
        number = 0.9
    if char == "W":
        number = 1.0
    if char == "X":
        number = 1.1
    if char == "Y":
        number = 1.2
    if char == "Z":
        number = 1.3
    if char == "[":
        number = 1.4
    if char == "\\":
        number = 1.5
    if char == "]":
        number = 1.6
    if char == "^":
        number = 1.7
    if char == "_":
        number = 1.8
    if char == "´":
        number = 1.9
    if char == "a":
        number = 2.0
    if char == "b":
        number = 2.1
    if char == "c":
        number = 2.2
    if char == "d":
        number = 2.3
    if char == "e":
        number = 2.4
    if char == "f":
        number = 2.5
    if char == "g":
        number = 2.6
    if char == "h":
        number = 2.7
    if char == "i":
        number = 2.8
    if char == "j":
        number = 2.9
    if char == "k":
        number = 3.0
    if char == "l":
        number = 3.1
    if char == "m":
        number = 3.2
    if char == "n":
        number = 3.3
    if char == "o":
        number = 3.4
    if char == "p":
        number = 3.5
    if char == "q":
        number = 3.6
    if char == "r":
        number = 3.7
    if char == "s":
        number = 3.8
    if char == "t":
        number = 3.9
    if char == "u":
        number = 4.0
    if char == "v":
        number = 4.1
    if char == "w":
        number = 4.2
    if char == "x":
        number = 4.3
    if char == "y":
        number = 4.4
    if char == "z":
        number = 4.5
    if char == "{":
        number = 4.6
    if char == "|":
        number = 4.7
    if char == "}":
        number = 4.8
    if char == "~":
        number = 4.9
    if char == "'":
        number = 5.0
   
    if number == None:    
        print ("The Code Contains An Error.")
        
    return number