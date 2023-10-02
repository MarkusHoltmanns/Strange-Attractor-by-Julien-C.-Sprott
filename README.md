# Strange-Attractor-by-Julien-C.-Sprott
Collection of Python Code for Creating Strange Attractors

This is my first great project I started in order to learn python. So, don't be mad if you see something strange in the code. Tell me what I can improve but so far it is working.

This project contains 4 python files.
1. StrangeAttractos.py is the main file.
2. The main file accesses the file functions.py where all the types of functions are defined.
3. Then a small python file named Code_Number_Converter.py that decodes the SABOOK-Code that Mr. Sprott uses in his book.
4. Then the SABOOK-Code, this file is called Code_Number.py

Each file should be simple enough and not totally overloaded... Therefore it keeps thing easy, I hope.

In the main file at line 18 the is a string called "char". That is where you put in the SABOOK-Code. The program then identifies the dimension of the map of the attractor, 
meaning is it an attractor with only one variable x (1D) or with two variables x and y (2D) or does it have a z-variable as well (3D).
While running the program it also saves the string "char" to name the image file which is going to be saved on your desktop. Please change the path in line 122 in the main 
file because your username is surely differnt from mine. The printed file name can be different if it contains characters that you can't use for naming
a image file like *, /, <, ? etc. Not to worry though, the correct code is saved in the image itself (top part) alongside the starting point (x, y and z value). With all that
you are able to recreate a neet attractor again if you change the code in the specific sections (x,y and z in lines 61 tp 63).

To get hands on the SABOOK-Codes given by Mr. Sprott you may look for yourself or take this pdf-file:
https://sprott.physics.wisc.edu/fractals/booktext/SABOOK.PDF by Julien C. Sprott (and his Strange Attractor Book).

Have fun and enjoy. 

