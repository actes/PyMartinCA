%% md

# HROT CA ... converting notations ... ranges to table to hexstring

(Type `shift+enter` (or the :arrow_forward: button above) to evaluate a chunk and move to the next. Press the :fast_forward: button to evaluate the entire notebook in one go.)  
((ctrl+a ctrl+c works ... for getting the entire source code))

%% py

import numpy as np

# M0 ... HROT


r=2
d=2*r+1

# example 1 : birth or survival 9-18
# to python ranges
list(range(9,19))

%% py

atable1=np.zeros( d*d , dtype=int)

atable1[9:19]=1

#('[0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0]')
#str(list(atable1))
str(atable1)

%% py
x=0
for i in range(d*d):
    if atable1[i] != 0:
        x=x|(1<<i)
        
#523776
#(x)

uintx2=x
uintx=x>>1

###hexstring1=format(uintx, '06x')
hexstring1=format(uintx, '0'+    str(r*(r+1))        +'x')

#('03ff00')
hexstring1


















========================================



s='b1e7108'
i=int(s, base=16)
s2=bin(i)
s2



g3r2
b1e7108
s3e7c80

r2b000008s000000		1
r2b000008s03ff00		1

r2b000108s00f500		1
r2b073108s05fc80		1
r2b1e7108s3e7c80		1

r3b0000dead0000s0000beef0000		1
r5b00000000000000000...000001fffffe00000000		1

r5
b0000000000000000001ffe00000000
s0000000000000001fffffe00000000
1fffffe00000000


p.push("HROT M");
            k.push(["Higher-Range Outer-Totalistic Moore", ""]);
            k.push(["Fredkin R2", "R2,C2,S0,2,4,6,8,10,12,14,16,18,20,22,24,B1,3,5,7,9,11,13,15,17,19,21,23"]);
            k.push(["Fredkin R3", "R3,C2,S0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,B1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47"]);
            k.push(["Fredkin R4", "R4,C2,S0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,B1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79"]);
            k.push(["Replicator R2", "R2,C2,S1,3,5,7,9,11,13,15,17,19,21,23,B1,3,5,7,9,11,13,15,17,19,21,23"]);
            k.push(["Replicator R3", "R3,C2,S1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,B1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47"]);
            k.push(["Replicator R4", "R4,C2,S1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,B1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79"]);





listlist1=[ [9,18] ]

s='b1e7108'
i=int(s, base=16)
s2=bin(i)
s2

%% js

a=1

//#ptrobj
//##jsresult.__builtins__
//#jsresult.iltins__
//#pyodide.globals.len()
//pyodide._module.glo



pyodide._module.ENV




