import os
import shape
import renderer

s = 0 # shape
r = 0 # renderer

dimension = ""

def showCmds():
    print("Type \"reset\" to reset any operations done after adding or deleting a point")
    if dimension == "2D":
        print("Type \"add x y\" to add a point to the graph")
        print("Type \"del\" to delete last inputted point")
        print("Type \"shear p v\" to shear the polygon (p = x/y) (v = float)")
        print("Type \"stretch p v\" to stretch the polygon (p = x/y) (v = float)")
        print("Type \"reflect p\" to reflect the polygon (p = x / x=-y / etc)")
        print("Type \"translate dx dy\" to translate the polygon (dx,dy = float)")
        print("Type \"rotate r p a b\"  to rotate the polygon, use p = z to perform default rotation on 2D. (r = float) (p = x/y/z) (a,b = float)")
        print("Type \"custom a b c d\" (2x2) to perform customized transformation matrix to the polygon")
    else:
        print("Type \"shear p v\" to shear the polygon (p = x/y/z) (v = float)")
        print("Type \"stretch p v\" to stretch the polygon (p = x/y/z) (v = float)")
        print("Type \"reflect p\" to reflect the polygon (p = x/x=-y/etc)")
        print("Type \"translate dx dy dz\" to translate the polygon (dx,dy = float)")
        print("Type \"rotate r p a b c\" to rotate the polygon (r = float) (p = x/y/z) (a,b,c = float)")
        print("Type \"custom a b c d e f g h i\" (3x3) to perform customized transformation matrix to the polygon")
    print("Type \"dilate v\" to scale the polygon (v = float)")
    print("Type \"exit\", \"stop\", or \"quit\" to quit the program")
    print("Make sure that your mouse pointer focus is on the GLUT window.")
    print("Type any command below:")
    print(">> ",end='',flush=True)

def welcomeScreen():
    global s, dimension
    
    os.system('cls')   
    print("________________/\\\\\\________________/\\\\\\\\\\\\_____/\\\\\\\\\\\\_________________________________        ")
    print(" _______________\\/\\\\\\_______________\\////\\\\\\____\\////\\\\\\_________________________________       ")
    print("  _______________\\/\\\\\\__________/\\\\\\____\\/\\\\\\_______\\/\\\\\\_________________________________      ")
    print("   _____/\\\\\\\\\\\\\\\\_\\/\\\\\\_________\\///_____\\/\\\\\\_______\\/\\\\\\_____/\\\\\\\\\\\\\\\\\\_____/\\\\\\____/\\\\\\_     ")
    print("    ___/\\\\\\//////__\\/\\\\\\\\\\\\\\\\\\\\___/\\\\\\____\\/\\\\\\_______\\/\\\\\\____\\////////\\\\\\___\\///\\\\\\/\\\\\\/__    ")
    print("     __/\\\\\\_________\\/\\\\\\/////\\\\\\_\\/\\\\\\____\\/\\\\\\_______\\/\\\\\\______/\\\\\\\\\\\\\\\\\\\\____\\///\\\\\\/____   ")
    print("      _\\//\\\\\\________\\/\\\\\\___\\/\\\\\\_\\/\\\\\\____\\/\\\\\\_______\\/\\\\\\_____/\\\\\\/////\\\\\\_____/\\\\\\/\\\\\\___  ")
    print("       __\\///\\\\\\\\\\\\\\\\_\\/\\\\\\___\\/\\\\\\_\\/\\\\\\__/\\\\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\\\\_\\//\\\\\\\\\\\\\\\\/\\\\__/\\\\\\/\\///\\\\\\_ ")
    print("        ____\\////////__\\///____\\///__\\///__\\/////////__\\/////////___\\////////\\//__\\///____\\///__")
    print()
    print("\t\t\t Welcome to the our lovely solution to")
    print("\t\t\t IF2123 Geometric Algebra's 2nd Big Mission")
    print()
    dimension = input('Please choose between "2D" or "3D": ')
    while ((dimension != "3D") and (dimension != "2D")):
        dimension = input('Please enter valid input ("2D" or "3D"): ')
    else:
        print("Your input is " + dimension)
    if (dimension == "3D"):
        s.points = [[100,100,100],[100,100,-100],[100,-100,100],[100,-100,-100],[-100,100,100],[-100,100,-100],[-100,-100,100],[-100,-100,-100]]
        s.points_backup = s.points[:]
        s.points_before = s.points[:]

# MAIN
s = shape.Shape()

welcomeScreen()
showCmds()

renderer = renderer.Renderer(s, dimension)
renderer.render()