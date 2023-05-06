from vpython import *
from vpython import *
while True:
    Str = input("Enter The Direction Ff The Current ! \n")
    Str1= input("Enter The Direction Of The Force ! \n")
    if ((Str != "entering") or (Str != "leaving")or(Str1!="Down")or(Str1!="Up")):
        break
a = []
if ((Str == "entering")and(Str1== "Down")):
    txt = text(text='this is the arrow for force ', pos=vector(5, 7, 0), align='left', color=color.yellow, height=1)
    txt2 = text(text='this is the arrow for current ', pos=vector(5, 3, 0), align='left', color=color.cyan, height=1)
    force = arrow(pos=vector(4, 7, 0), axis=vector(0, -4, 0), color=color.yellow)
    current = arrow(pos=vector(4, 7, 0), axis=vector(0, 0, -4), color=color.cyan)
    T1 = cylinder(axis=vector(0, 20, 0), color=color.red, align='center', length=12, width=0.8, height=0.8)
    for i in range(1, 9):
        a1 = arrow(pos=vector(-1, i, 0), axis=vector(1, 0, -1), color=color.white)
        a.append(a1)
        a2 = arrow(pos=vector(0, i, -1), axis=vector(1, 0, 1), color=color.white)
        a.append(a2)
        a3 = arrow(pos=vector(1, i, 0), axis=vector(-1, 0, 1), color=color.white)
        a.append(a3)
        a4 = arrow(pos=vector(0, i, 1), axis=vector(-1, 0, -1), color=color.white)
        a.append(a4)
        a5 = arrow(pos=vector(0, i, 1), axis=vector(-1, 0, -1), color=color.white)
        a.append(a5)
        a6 = arrow(pos=vector(0, i, 1), axis=vector(-1, 0, -1), color=color.white)
        a.append(a6)
        a7 = arrow(pos=vector(0, i, 1), axis=vector(-1, 0, -1), color=color.white)
        a.append(a7)
# leaving
#entering and UP
if ((Str == "leaving")and(Str1== "Down")):
    T1 = cylinder(axis=vector(0, 20, 0), color=color.red, length=12, width=0.8, height=0.8)

    txt = text(text='this is the arrow for force ', pos=vector(5, 7, 0), align='left', color=color.yellow, height=1)
    txt2 = text(text='this is the arrow for current ', pos=vector(5, 3, 0), align='left', color=color.cyan, height=1)

    force = arrow(pos=vector(4, 7, 0), axis=vector(0, 4, 0), color=color.yellow)
    current = arrow(pos=vector(4, 7, 0), axis=vector(0, 0, 4), color=color.cyan)
    for i in range(1, 9):
        a1 = arrow(pos=vector(-1, i, 0), axis=vector(1, 0, 1), color=color.white)
        a.append(a1)
        a2 = arrow(pos=vector(0, i, -1), axis=vector(-1, 0, 1), color=color.white)
        a.append(a2)
        a3 = arrow(pos=vector(1, i, 0), axis=vector(-1, 0, -1), color=color.white)
        a.append(a3)
        a4 = arrow(pos=vector(0, i, 1), axis=vector(1, 0, -1), color=color.white)
        a.append(a4)
while True:
    pass
