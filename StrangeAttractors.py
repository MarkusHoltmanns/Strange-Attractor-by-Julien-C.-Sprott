"""
This program is based on the Book by Julien C. Sprott: 
Strange Attractors: Creating Patterns in Chaos

This Book (pdf file found with the name SABOOK) contains the equations, the variables
and a Code for the values of those variables.
Furthermore you can also read some code-line which might help you while coding.
Have fun and use the list of Codes (examples of attractors).
"""
import matplotlib.pyplot as plt
import numpy as np
import functions
import random
from textwrap import wrap



char = "VMMKMRMREPCPYAFRGJBOTPHNQRFXVNSNYQVJNBXXPKRPVHFQAFGFSTHYFKCIDWXOQJAKRFKHPYHNENTDQLJMQGMXTFPBDFUIPAIODWYAMTXJDIWGERTHDOKWFXPLSWFYPXNQMNOBKILSG" # "VHETJPMKNMHQNUVBIOTFADJUXXIQRSGDSNXAGNEKPMCJRIDEHOFTVTPLWUFLNDCWLKHXKKELUMBDOHSIBSDEWWSPLQVMWLQERMCANDUBCXULQWYGOTLGLLQFSJGVQEUIEQQXXWGEKVTPA" # "UBLFBKKFNATJVTJUKJFGALBIPQHVRUMAROTNVHBLAQVSHVHRGLFJAAABFRJFW" # "JJICKAFXIOXFVGOCIDNIVRPSFYPFGABXKKONQWPAMJGKAGXDBBWFHGXBTPNVD" # "EWM?MPMMWMMMM" #"EZPMSGCNFRENG" #"AXBH"
print(char)
dimension = 0
type_of_attractor = None
torus = False # True
if torus ==True:
    print("Torus from a .", end='')
    
if char[0] == "A" or char[0] =="B" or char[0] =="C" or char[0] =="D":
    dimension = 1
    if char[0] == "A":
        type_of_attractor = "quadratic"
    if char[0] == "B":
        type_of_attractor = "cubic"
    if char[0] == "C":
        type_of_attractor = "quartic"
    if char[0] == "D":
        type_of_attractor = "quintic"

    print("1D "+type_of_attractor+" map.")
if char[0] == "E" or char[0] =="F" or char[0] =="G" or char[0] =="H":
    dimension = 2
    if char[0] == "E":
        type_of_attractor = "quadratic"
    if char[0] == "F":
        type_of_attractor = "cubic"
    if char[0] == "G":
        type_of_attractor = "quartic"
    if char[0] == "H":
        type_of_attractor = "quintic"
    print("2D "+type_of_attractor+" map.")
if char[0] == "I" or char[0] =="J" or char[0] =="K" or char[0] =="L":
    dimension = 3
    if char[0] == "I":
        type_of_attractor = "quadratic"
    if char[0] == "J":
        type_of_attractor = "cubic"
    if char[0] == "K":
        type_of_attractor = "quartic"
    if char[0] == "L":
        type_of_attractor = "quintic"
    print("3D "+type_of_attractor+" map.")
if char[0] == "M" or char[0] =="N" or char[0] =="O" or char[0] =="P":
    dimension = 4
    if char[0] == "M":
        type_of_attractor = "quadratic"
    if char[0] == "N":
        type_of_attractor = "cubic"
    if char[0] == "O":
        type_of_attractor = "quartic"
    if char[0] == "P":
        type_of_attractor = "quintic"
    print("4D "+type_of_attractor+" map.")
if char[0] == "Q" or char[0] =="R" or char[0] =="S" or char[0] =="T":
    dimension = 3
    if char[0] == "Q":
        type_of_attractor = "quadratic"
    if char[0] == "R":
        type_of_attractor = "cubic"
    if char[0] == "S":
        type_of_attractor = "quartic"
    if char[0] == "T":
        type_of_attractor = "quintic"
    print("3D "+type_of_attractor+" ODE.")
if char[0] == "U" or char[0] =="V" or char[0] =="W" or char[0] =="X":
    dimension = 4
    if char[0] == "U":
        type_of_attractor = "quadratic ODE"
    if char[0] == "V":
        type_of_attractor = "cubic ODE"
    if char[0] == "W":
        type_of_attractor = "quartic ODE"
    if char[0] == "X":
        type_of_attractor = "quintic ODE"
    print("4D "+type_of_attractor+".")
if char[0] == "Y" or char[0] =="Z" or char[0] =="[":
    dimension = 3
    print("3D modulus map.")
if char[0] =="\\"or char[0] =="]"or char[0] =="^":
    dimension = 3
    print("3D trigonometrical map.")

    
stop = 1
run = 0
while run < stop:
    print ("run = ", run)
    x = random.uniform(-0.1,0.1)
    y = random.uniform(-0.1,0.1)
    z = random.uniform(-0.1,0.1)
    w = random.uniform(-0.1,0.1)
    variables = (x,y,z,w)
    x_vals = []
    y_vals = []
    z_vals = []
    w_vals = []
    i = 0
    n = 50000
    n_temp = n
    dt = 0.01
    while i < n_temp:
        variables = functions.function(char,variables,dt)
        conditions = 0
        if dimension >= 1:
            x_vals.append( variables[0])
            conditions = x_vals[i]*x_vals[i]
        if dimension >= 2:
            y_vals.append( variables[1])
            conditions = conditions + y_vals[i]*y_vals[i]
        if dimension >= 3:
            z_vals.append( variables[2])
            conditions = conditions + z_vals[i]*z_vals[i]
        if dimension >= 4:
            w_vals.append( variables[3])
            conditions = conditions + w_vals[i]*w_vals[i]
        #print(x_vals[i],y_vals[i],z_vals[i])
        
        i=i+1 
        if conditions > 100:
            print("conditions wasn't met because absolute value of conditions = ", conditions)
            n_temp = i
            stop = stop + 1
    run = run + 1

filename_sub = None
if dimension == 2:
    plt.subplots(dpi = 250)
    plt.scatter(x_vals, y_vals, s = 0.05, facecolors = 'blue', edgecolors = 'none')
    plt.xlabel("X Axis", fontsize=8)
    plt.ylabel("Y Axis", fontsize=8)
    filename_sub = "2D-"+type_of_attractor+"-attractor-"+char+")"
    plt.title("2D-"+type_of_attractor+" attractor: (x$_{0}$,y$_{0}$)=(%f" %x + ",%f" %y + ")")
    new_string = "SABOOK-Code: "+char
    plt.text(0, 1.75, s="\n".join(wrap(new_string)),fontsize=5, horizontalalignment="center")
  
if dimension >= 3:
    fig = plt.figure(dpi = 250)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.scatter(x_vals, y_vals, z_vals, s = 0.05, facecolors = 'blue', edgecolors = 'none')
    ax.set_xlabel("X Axis", fontsize=8)
    ax.set_ylabel("Y Axis", fontsize=8)
    ax.set_zlabel("Z Axis", fontsize=8)
    filename_sub = "3D-"+type_of_attractor+"-attractor-"+char+")"
    ax.set_title("3D-"+type_of_attractor+" attractor: (x$_{0}$,y$_{0}$,z$_{0}$)=(%f" %x + ",%f" %y + ",%f" %z +")")
    new_string = "SABOOK-Code: "+char
    fig.text(0.5, 0.94, s="\n".join(wrap(new_string)),fontsize=5, horizontalalignment="center")

plt.axis('square')
plt.axis('scaled')

bad_chars = [';', ':', '!', "?", "*", " ", "*", "\\", "/", "|", "<", ">"]
for i in bad_chars:
	filename_sub = filename_sub.replace(i, '')

filename = "/Users/Holtmanns/Desktop/"+filename_sub+".png"
plt.savefig(filename, dpi=1000)
plt.show()
print("Done.")