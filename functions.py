import numpy as np
import math
import Code_Number_Converter

def function(char, oldvariables):
    # in the SABOOK L and F are numbers that represent die Fractal Dimension F = logs2(N1/N2) = sum log2(df/dx)/N 1-L1/L2 and the Lyapunov Dimension L
    variables = None
    
    aa = []
    aa = Code_Number_Converter.Converted_Number(char)
    a = np.empty((len(aa)+1,1))
    a[0] = (0)
    for i in range(len(aa)):
        a[i+1] = aa[i]
        
    # A = 1D quadratic map
    if char[0] == "A":
        x = oldvariables[0]
        X = a[1] + a[2]*x + a[3]*np.power(x,2)
        variables = (X)
    # B = 1D cubic map
    if char[0] == "B":
        x = oldvariables[0]
        X = a[1] + a[2]*x + a[3]*np.power(x,2) + a[4]*np.power(x,3)
        variables = (X)
    # C = 1D quartic map
    if char[0] == "C":
        x = oldvariables[0]
        X = a[1] + a[2]*x + a[3]*np.power(x,2) + a[4]*np.power(x,3) + a[5]*np.power(x,4)
        variables = (X)
    # D = 1D quintic map
    if char[0] == "D":
        x = oldvariables[0]
        X = a[1] + a[2]*x + a[3]*np.power(x,2) + a[4]*np.power(x,3) + a[5]*np.power(x,4) + a[6]*np.power(x,5)
        variables = (X)
    # E = 2D quadratic map
    if char[0] == "E":
        x = oldvariables[0]
        y = oldvariables[1]
        X = a[1] + a[2]*x + a[3]*np.power(x,2) +  a[4]*x*y +  a[5]*y +  a[6]*np.power(y,2)
        Y = a[7] + a[8]*x + a[9]*np.power(x,2) + a[10]*x*y + a[11]*y + a[12]*np.power(y,2)
        variables = (X,Y)
    # F = 2D cubic map
    if char[0] == "F":
        x = oldvariables[0]
        y = oldvariables[1]
        X =  a[1] +  a[2]*x +  a[3]*np.power(x,2) +  a[4]*np.power(x,3) +  a[5]*np.power(x,2)*y +  a[6]*x*y +  a[7]*x*np.power(y,2) +  a[8]*y +  a[9]*np.power(y,2) + a[10]*np.power(y,3) 
        Y = a[11] + a[12]*x + a[13]*np.power(x,2) + a[14]*np.power(x,3) + a[15]*np.power(x,2)*y + a[16]*x*y + a[17]*x*np.power(y,2) + a[18]*y + a[19]*np.power(y,2) + a[20]*np.power(y,3) 
        variables = (X,Y)
    # G = 2D quartic map
    if char[0] == "G":
        x = oldvariables[0]
        y = oldvariables[1]
        X =  a[1] +  a[2]*x +  a[3]*np.power(x,2) +  a[4]*np.power(x,3) +  a[5]*np.power(x,4) +  a[6]*np.power(x,3)*y +  a[7]*np.power(x,2)*y +  a[8]*np.power(x,2)*np.power(y,2) +  a[9]*x*y + a[10]*x*np.power(y,2) + a[11]*x*np.power(y,3) + a[12]*y + a[13]*np.power(y,2) + a[14]*np.power(y,3) + a[15]*np.power(y,4)
        Y = a[16] + a[17]*x + a[18]*np.power(x,2) + a[19]*np.power(x,3) + a[20]*np.power(x,4) + a[21]*np.power(x,3)*y + a[22]*np.power(x,2)*y + a[23]*np.power(x,2)*np.power(y,2) + a[24]*x*y + a[25]*x*np.power(y,2) + a[26]*x*np.power(y,3) + a[27]*y + a[28]*np.power(y,2) + a[29]*np.power(y,3) + a[30]*np.power(y,4)
        variables = (X,Y)
    # H = 2D quintic map
    if char[0] == "H":
        x = oldvariables[0]
        y = oldvariables[1]
        X =  a[1] +  a[2]*x +  a[3]*np.power(x,2) +  a[4]*np.power(x,3) +  a[5]*np.power(x,4) +  a[6]*np.power(x,5) +  a[7]*np.power(x,4)*y +  a[8]*np.power(x,3)*y +  a[9]*np.power(x,3)*np.power(y,2) + a[10]*np.power(x,2)*y + a[11]*np.power(x,2)*np.power(y,2) + a[12]*np.power(x,2)*np.power(y,3) + a[13]*x*y + a[14]*x*np.power(y,2) + a[15]*x*np.power(y,3) + a[16]*x*np.power(y,4) + a[17]*y + a[18]*np.power(y,2) + a[19]*np.power(y,3) + a[20]*np.power(y,4) + a[21]*np.power(y,5)
        Y = a[22] + a[23]*x + a[24]*np.power(x,2) + a[25]*np.power(x,3) + a[26]*np.power(x,4) + a[27]*np.power(x,5) + a[28]*np.power(x,4)*y + a[29]*np.power(x,3)*y + a[30]*np.power(x,3)*np.power(y,2) + a[31]*np.power(x,2)*y + a[32]*np.power(x,2)*np.power(y,2) + a[33]*np.power(x,2)*np.power(y,3) + a[34]*x*y + a[35]*x*np.power(y,2) + a[36]*x*np.power(y,3) + a[37]*x*np.power(y,4) + a[38]*y + a[39]*np.power(y,2) + a[40]*np.power(y,3) + a[41]*np.power(y,4) + a[42]*np.power(y,5)
        variables = (X,Y)
    # I = 3D quadratic map
    if char[0] == "I":
        x = oldvariables[0]
        y = oldvariables[1]
        z = oldvariables[2]
        X =  a[1] +  a[2]*x +  a[3]*np.power(x,2) +  a[4]*x*y +  a[5]*x*z +  a[6]*y +  a[7]*np.power(y,2) +  a[8]*y*z +  a[9]*z + a[10]*np.power(z,2)
        Y = a[11] + a[12]*x + a[13]*np.power(x,2) + a[14]*x*y + a[15]*x*z + a[16]*y + a[17]*np.power(y,2) + a[18]*y*z + a[19]*z + a[20]*np.power(z,2)
        Z = a[21] + a[22]*x + a[23]*np.power(x,2) + a[24]*x*y + a[25]*x*z + a[26]*y + a[27]*np.power(y,2) + a[28]*y*z + a[29]*z + a[30]*np.power(z,2)
        variables = (X,Y,Z)
    # J = 3D cubic map
    if char[0] == "J":
        x = oldvariables[0]
        y = oldvariables[1]
        z = oldvariables[2]
        X =  a[1] +  a[2]*x +  a[3]*np.power(x,2) +  a[4]*np.power(x,3) +  a[5]*np.power(x,2)*y +  a[6]*np.power(x,2)*z +  a[7]*x*y +  a[8]*x*np.power(y,2) +  a[9]*x*y*z + a[10]*x*z + a[11]*x*np.power(z,2) + a[12]*y + a[13]*np.power(y,2) + a[14]*np.power(y,3) + a[15]*np.power(y,2)*z + a[16]*y*z + a[17]*y*np.power(z,2) + a[18]*z + a[19]*np.power(z,2) + a[20]*np.power(z,3)
        Y = a[21] + a[22]*x + a[23]*np.power(x,2) + a[24]*np.power(x,3) + a[25]*np.power(x,2)*y + a[26]*np.power(x,2)*z + a[27]*x*y + a[28]*x*np.power(y,2) + a[29]*x*y*z + a[30]*x*z + a[31]*x*np.power(z,2) + a[32]*y + a[33]*np.power(y,2) + a[34]*np.power(y,3) + a[35]*np.power(y,2)*z + a[36]*y*z + a[37]*y*np.power(z,2) + a[38]*z + a[39]*np.power(z,2) + a[40]*np.power(z,3)
        Z = a[41] + a[42]*x + a[43]*np.power(x,2) + a[44]*np.power(x,3) + a[45]*np.power(x,2)*y + a[46]*np.power(x,2)*z + a[47]*x*y + a[48]*x*np.power(y,2) + a[49]*x*y*z + a[50]*x*z + a[51]*x*np.power(z,2) + a[52]*y + a[53]*np.power(y,2) + a[54]*np.power(y,3) + a[55]*np.power(y,2)*z + a[56]*y*z + a[57]*y*np.power(z,2) + a[58]*z + a[59]*np.power(z,2) + a[60]*np.power(z,3)
        variables = (X,Y,Z)
    # K = 3D quartic map
    if char[0] == "K":
        x = oldvariables[0]
        y = oldvariables[1]
        z = oldvariables[2]
        X =  a[1] +  a[2]*x +  a[3]*np.power(x,2) +  a[4]*np.power(x,3) +  a[5]*np.power(x,4) +  a[6]*np.power(x,3)*y +  a[7]*np.power(x,3)*z +  a[8]*np.power(x,2)*y +  a[9]*np.power(x,2)*np.power(y,2) + a[10]*np.power(x,2)*y*z + a[11]*np.power(x,2)*z + a[12]*np.power(x,2)*np.power(z,2) + a[13]*x*y + a[14]*x*np.power(y,2) + a[15]*x*np.power(y,3) + a[16]*x*np.power(y,2)*z + a[17]*x*y*z + a[18]*x*y*np.power(z,2) + a[19]*x*z + a[20]*x*np.power(z,2) + a[21]*x*np.power(z,3) + a[22]*y + a[23]*np.power(y,2) + a[24]*np.power(y,3) + a[25]*np.power(y,4) + a[26]*np.power(y,3)*z + a[27]*np.power(y,2)*z + a[28]*np.power(y,2)*np.power(z,2) + a[29]*y*z +  a[30]*y*np.power(z,2) +  a[31]*y*np.power(z,3) +  a[32]*z +  a[33]*np.power(z,2) +  a[34]*np.power(z,3) + a[35]*np.power(z,4)
        Y = a[36] + a[37]*x + a[38]*np.power(x,2) + a[39]*np.power(x,3) + a[40]*np.power(x,4) + a[41]*np.power(x,3)*y + a[42]*np.power(x,3)*z + a[43]*np.power(x,2)*y + a[44]*np.power(x,2)*np.power(y,2) + a[45]*np.power(x,2)*y*z + a[46]*np.power(x,2)*z + a[47]*np.power(x,2)*np.power(z,2) + a[48]*x*y + a[49]*x*np.power(y,2) + a[50]*x*np.power(y,3) + a[51]*x*np.power(y,2)*z + a[52]*x*y*z + a[53]*x*y*np.power(z,2) + a[54]*x*z + a[55]*x*np.power(z,2) + a[56]*x*np.power(z,3) + a[57]*y + a[58]*np.power(y,2) + a[59]*np.power(y,3) + a[60]*np.power(y,4) + a[61]*np.power(y,3)*z + a[62]*np.power(y,2)*z + a[63]*np.power(y,2)*np.power(z,2) + a[64]*y*z +  a[65]*y*np.power(z,2) +  a[66]*y*np.power(z,3) +  a[67]*z +  a[68]*np.power(z,2) +  a[69]*np.power(z,3) + a[70]*np.power(z,4)
        Z = a[71] + a[72]*x + a[73]*np.power(x,2) + a[74]*np.power(x,3) + a[75]*np.power(x,4) + a[76]*np.power(x,3)*y + a[77]*np.power(x,3)*z + a[78]*np.power(x,2)*y + a[79]*np.power(x,2)*np.power(y,2) + a[80]*np.power(x,2)*y*z + a[81]*np.power(x,2)*z + a[82]*np.power(x,2)*np.power(z,2) + a[83]*x*y + a[84]*x*np.power(y,2) + a[85]*x*np.power(y,3) + a[86]*x*np.power(y,2)*z + a[87]*x*y*z + a[88]*x*y*np.power(z,2) + a[89]*x*z + a[90]*x*np.power(z,2) + a[91]*x*np.power(z,3) + a[92]*y + a[93]*np.power(y,2) + a[94]*np.power(y,3) + a[95]*np.power(y,4) + a[96]*np.power(y,3)*z + a[97]*np.power(y,2)*z + a[98]*np.power(y,2)*np.power(z,2) + a[99]*y*z + a[100]*y*np.power(z,2) + a[101]*y*np.power(z,3) + a[102]*z + a[103]*np.power(z,2) + a[104]*np.power(z,3) + a[105]*np.power(z,4)
        variables = (X,Y,Z)
    # L = 3D quintic map
    if char[0] == "L":
        x = oldvariables[0]
        y = oldvariables[1]
        z = oldvariables[2]
        X =   a[1] +   a[2]*x +   a[3]*np.power(x,2) +   a[4]*np.power(x,3) +   a[5]*np.power(x,4) +   a[6]*np.power(x,5) +   a[7]*np.power(x,4)*y +   a[8]*np.power(x,4)*z +   a[9]*np.power(x,3)*y +  a[10]*np.power(x,3)*np.power(y,2) + a[11]*np.power(x,3)*y*z +  a[12]*np.power(x,3)*z +  a[13]*np.power(x,3)*np.power(z,2) +  a[14]*np.power(x,2)*y +  a[15]*np.power(x,2)*np.power(y,2) +  a[16]*np.power(x,2)*np.power(y,3) +  a[17]*np.power(x,2)*np.power(y,2)*z +  a[18]*np.power(x,2)*y*z +  a[19]*np.power(x,2)*y*np.power(z,2) +  a[20]*np.power(x,2)*z +  a[21]*np.power(x,2)*np.power(z,2) +  a[22]*np.power(x,2)*np.power(z,3) +  a[23]*x*y +  a[24]*x*np.power(y,2) +  a[25]*x*np.power(y,3) +  a[26]*x*np.power(y,4) +  a[27]*x*np.power(y,3)*z +  a[28]*x*np.power(y,2)*z +  a[29]*x*np.power(y,2)*np.power(z,2) +  a[30]*x*y*z +  a[31]*x*y*np.power(z,2) +  a[32]*x*y*np.power(z,3) +  a[33]*x*z +  a[34]*x*np.power(z,2) +  a[35]*x*np.power(z,3) +  a[36]*x*np.power(z,4) +  a[37]*y +  a[38]*np.power(y,2) +  a[39]*np.power(y,3) +  a[40]*np.power(y,4) +  a[41]*np.power(y,5) +  a[42]*np.power(y,4)*z +  a[43]*np.power(y,3)*z +  a[44]*np.power(y,3)*np.power(z,2) +  a[45]*np.power(y,2)*z +  a[46]*np.power(y,2)*np.power(z,2) +  a[47]*np.power(y,2)*np.power(z,3) +  a[48]*y*z +  a[49]*y*np.power(z,2) +  a[50]*y*np.power(z,3) +  a[51]*y*np.power(z,4) +  a[52]*z +  a[53]*np.power(z,2) +  a[54]*np.power(z,3) +  a[55]*np.power(z,4) +  a[56]*np.power(z,5)
        Y =  a[57] +  a[58]*x +  a[59]*np.power(x,2) +  a[60]*np.power(x,3) +  a[61]*np.power(x,4) +  a[62]*np.power(x,5) +  a[63]*np.power(x,4)*y +  a[64]*np.power(x,4)*z +  a[65]*np.power(x,3)*y +  a[66]*np.power(x,3)*np.power(y,2) + a[67]*np.power(x,3)*y*z +  a[68]*np.power(x,3)*z +  a[69]*np.power(x,3)*np.power(z,2) +  a[70]*np.power(x,2)*y +  a[71]*np.power(x,2)*np.power(y,2) +  a[72]*np.power(x,2)*np.power(y,3) +  a[73]*np.power(x,2)*np.power(y,2)*z +  a[74]*np.power(x,2)*y*z +  a[75]*np.power(x,2)*y*np.power(z,2) +  a[76]*np.power(x,2)*z +  a[77]*np.power(x,2)*np.power(z,2) +  a[78]*np.power(x,2)*np.power(z,3) +  a[79]*x*y +  a[80]*x*np.power(y,2) +  a[81]*x*np.power(y,3) +  a[82]*x*np.power(y,4) +  a[83]*x*np.power(y,3)*z +  a[84]*x*np.power(y,2)*z +  a[85]*x*np.power(y,2)*np.power(z,2) +  a[86]*x*y*z +  a[87]*x*y*np.power(z,2) +  a[88]*x*y*np.power(z,3) +  a[89]*x*z +  a[90]*x*np.power(z,2) +  a[91]*x*np.power(z,3) +  a[92]*x*np.power(z,4) +  a[93]*y +  a[94]*np.power(y,2) +  a[95]*np.power(y,3) +  a[96]*np.power(y,4) +  a[97]*np.power(y,5) +  a[98]*np.power(y,4)*z +  a[99]*np.power(y,3)*z + a[100]*np.power(y,3)*np.power(z,2) + a[101]*np.power(y,2)*z + a[102]*np.power(y,2)*np.power(z,2) + a[103]*np.power(y,2)*np.power(z,3) + a[104]*y*z + a[105]*y*np.power(z,2) + a[106]*y*np.power(z,3) + a[107]*y*np.power(z,4) + a[108]*z + a[109]*np.power(z,2) + a[110]*np.power(z,3) + a[111]*np.power(z,4) + a[112]*np.power(z,5)
        Z = a[113] + a[114]*x + a[115]*np.power(x,2) + a[116]*np.power(x,3) + a[117]*np.power(x,4) + a[118]*np.power(x,5) + a[119]*np.power(x,4)*y + a[120]*np.power(x,4)*z + a[121]*np.power(x,3)*y + a[122]*np.power(x,3)*np.power(y,2)+ a[123]*np.power(x,3)*y*z + a[124]*np.power(x,3)*z + a[125]*np.power(x,3)*np.power(z,2) + a[126]*np.power(x,2)*y + a[127]*np.power(x,2)*np.power(y,2) + a[128]*np.power(x,2)*np.power(y,3) + a[129]*np.power(x,2)*np.power(y,2)*z + a[130]*np.power(x,2)*y*z + a[131]*np.power(x,2)*y*np.power(z,2) + a[132]*np.power(x,2)*z + a[133]*np.power(x,2)*np.power(z,2) + a[134]*np.power(x,2)*np.power(z,3) + a[135]*x*y + a[136]*x*np.power(y,2) + a[137]*x*np.power(y,3) + a[138]*x*np.power(y,4) + a[139]*x*np.power(y,3)*z + a[140]*x*np.power(y,2)*z + a[141]*x*np.power(y,2)*np.power(z,2) + a[142]*x*y*z + a[143]*x*y*np.power(z,2) + a[144]*x*y*np.power(z,3) + a[145]*x*z + a[146]*x*np.power(z,2) + a[147]*x*np.power(z,3) + a[148]*x*np.power(z,4) + a[149]*y + a[150]*np.power(y,2) + a[151]*np.power(y,3) + a[152]*np.power(y,4) + a[153]*np.power(y,5) + a[154]*np.power(y,4)*z + a[155]*np.power(y,3)*z + a[156]*np.power(y,3)*np.power(z,2) + a[157]*np.power(y,2)*z + a[158]*np.power(y,2)*np.power(z,2) + a[159]*np.power(y,2)*np.power(z,3) + a[160]*y*z + a[161]*y*np.power(z,2) + a[162]*y*np.power(z,3) + a[163]*y*np.power(z,4) + a[164]*z + a[165]*np.power(z,2) + a[166]*np.power(z,3) + a[167]*np.power(z,4) + a[168]*np.power(z,5)
        variables = (X,Y,Z)
        
        
    return variables