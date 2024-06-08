from turtle import *

'''
TURTLE MOTION
    A) 4 Direction to Moving the turtle
        1) forward() | fd()                             --> maju sebanyak (distance) langkah
        2) right() | rt()                               --> hadap kanan / belok kanan sebanyak (angle) derajat
        3) back() | backward() | bk()                   --> mundur sebanyak (distance) langkah
        4) left() | lt()                                --> hadap kiri / belok kiri sebanyak (angle) derajat
'''
# SEGITIGA
# forward(100)                          
# left(120)                           
# forward(100)
# left(120)
# forward(100)

# JAJAR GENJANG
# forward(100)                            
# left(120)
# forward(100)
# right(120)                              
# backward(100)                           
# left(120)
# backward(100)

# TRAPESIUM
# forward(100)                            
# left(120)
# forward(100)
# right(120)                              
# backward(100)                           
# left(60)
# backward(100)
# left(120)
# backward(100)

'''
Preset Figure
    1) circle()                     --> menggambar lingkaran
    2) dot()                        --> menggambar titik
'''
# circle(90)
# dot(20)

'''
PEN CONTROL
    1) color('...')     --> mengubah warna pen
    2) width()          --> mengubah size/lebar pen
    3) up()             --> mengangkat pen
    4) down()           --> menurunkan pen
'''
# color("red")
# width(5)                           
# up()
# forward(100)    
# left(90)                         
# down()                           
# forward(100)
# left(90)
# up()
# forward(100)
# left(90)
# width(15)
# color("blue")
# down()
# forward(100)

'''
Turtle Position
    1) home()           --> mengembalikan posisi ke tengah, koordinatnya di (0,0)
    2) pos()            --> jika ingin mengetahui koordinat turtle
    3) clearscreen()    --> menghapus window 
'''
# fd(100)
# home()
# bk(100)
# lt(90)
# fd(100)
# print(pos())
# clearscreen()
# rt(90)
# fd(100)
