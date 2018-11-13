import os
import shape
import renderer

s = 0 # shape
r = 0 # renderer

dimension = ""

def showCmds():
    print("Type \"exit\", \"stop\", or \"quit\" to quit the program")
    print("Type \"add x y z\" or \"add x y\" to add a point to the graph")
    print("Type \"del\" to delete last inputted point")
    print("Type \"reset\" to reset any operations done after adding or deleting a point")
    print("Type \"dilate v\" to scale the polygon (v = float)")
    print("Type \"shear p v\" to shear the polygon (p = x/y/z) (v = float)")
    print("Type \"stretch p v\" to stretch the polygon (p = x/y/z) (v = float)")
    print("Type \"reflect p\" to reflect the polygon (p = x/x=-y/etc)")
    print("Type \"translate dx dy dz\" to translate the polygon (dx,dy,dz = float)")
    print("Type \"rotate r p a b\" or \"rotate r p a b c\" to rotate the polygon (r = float) (p = x/y/z) (a,b,c = float)")
    print("Type \"custom a b c d\" (2x2) or \"custom a b c d e f g h i\" (3x3) to perform customized transformation matrix to the polygon")
    print("Type any command below:")
    print(">> ",end='',flush=True)

def welcomeScreen():
    global s, dimension
    
    os.system('cls')
    print("\t\t\t Selamat Datang")
    print("\t\t\t Di Aplikasi Tugas Besar 2")
    print("\t\t\t IF 2123 Aljabar Geometri")
    dimension = input("Silahkan pilih, antara '2D' atau '3D' : ")
    while ((dimension != "3D") and (dimension != "2D")):
        dimension = input("Masukan input yang tepat : ")
    else:
        print("Anda memasukan %s", dimension)
    if (dimension == "3D"):
        print("Blah")
        s.points = [[100,100,100],[100,100,-100],[100,-100,100],[100,-100,-100],[-100,100,100],[-100,100,-100],[-100,-100,100],[-100,-100,-100]]
        s.points_backup = s.points[:]
        s.points_before = s.points[:]

# MAIN
s = shape.Shape()

welcomeScreen()
showCmds()

renderer = renderer.Renderer(s, dimension)
renderer.render()