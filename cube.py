from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

Z_TRANSLATE = -2000.0 # To translate into viewport

window = 0
points = []

def InitGL(Width, Height):                
    glClearColor(0, 0, 0, 0.0)    
    glClearDepth(1.0)                   
    glDepthFunc(GL_LESS)                
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT, GL_FILL)    
    glPolygonMode(GL_BACK, GL_FILL)     
    glShadeModel(GL_SMOOTH)                
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                   
    gluPerspective(45, float(Width)/float(Height), 0.1, 2 * Z_TRANSLATE)
    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                       
        Height = 1

    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(Width)/float(Height), 0.1, 2 * Z_TRANSLATE)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global points

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()
    glTranslatef(0.0,0.0,Z_TRANSLATE)        
    glBegin(GL_POLYGON)
    
    for point in points:
        glColor3f(1,1,1)
        glVertex3f(point[0], point[1], point[2])
    
    glEnd()                 
    
    glutSwapBuffers()

def showCmds():
    print("Type \"exit\", \"stop\", or \"quit\" to quit the program")
    print("Type \"add x y z\" or \"add x y\" to add a point to the graph")
    print("Type \"del\" to delete last inputted point")
    print("Type \"dilate v\" to scale the polygon (v = float)")
    print("Type \"shear p v\" to shear the polygon (p = x/y/z) (v = float)")
    print("Type any command below:")
    print(">> ",end='',flush=True)
    
def addLine(line):
    global points
    newline = []
    newline = newline + [float(line[0])]
    newline = newline + [float(line[1])]
    try:
        newline = newline + [float(line[2])]
    except IndexError:
        newline = newline + [0]
    
    points = points + [newline]

def delLine():
    global points
    points = points[:-1]

def dilate(multiplier):
    global points
    newpoints = []
    for point in points:
        newpoint = []
        for number in point:
            newpoint += [number * float(multiplier)]
        newpoints += [newpoint]
    points = newpoints
    
def shear(param, value):
    value = float(value)
    global points
    newpoints = []
    for point in points:
        num = point
        if (param == 'x'):
            num[0] += value*num[1] + value*num[2]
        if (param == 'y'):
            num[1] += value*num[0] + value*num[2]
        if (param == 'z'):
            num[2] += value*num[0] + value*num[1]
        newpoints += [[num[0], num[1], num[2]]]
    points = newpoints
    
def stretch(param, value):
    value = float(value)
    global points
    newpoints = []
    for point in points:
        num = point
        if (param == 'x'):
            num[0] = num[0]*value
        if (param == 'y'):
            num[1] = num[1]*value
        if (param == 'z'):
            num[2] =num[2]*value
        newpoints += [[num[0], num[1], num[2]]]
    points = newpoints

def reflect(param):
    global points
    newpoints = []
    for point in points:
        num = point
        if (param == 'x'):
            num[1] = -num[1]
            num[2] = -num[2]
        elif (param == 'y'):
            num[0] = -num[0]
            num[2] = -num[2]
        elif (param == 'z'):
            num[0] = -num[0]
            num[1] = -num[1]
        elif (param == 'y=x'):
            swap = num[0]
            num[0] = num[1]
            num[1] = swap
            num[2] = -num[2]
        elif (param == 'y=-x'):
            swap = -num[0]
            num[0] = -num[1]
            num[1] = swap
            num[2] = -num[2]
        else:
            param = param[1:-1].split(',')
        newpoints += [[num[0], num[1], num[2]]]
    points = newpoints


def doCmd(cmds):
    #cmds[0] = kata pertama
    #cmds[1] = kata kedua, dst
    try:
        if cmds[0] == "exit": exit()
        if cmds[0] == "stop": exit()
        if cmds[0] == "quit": exit()
        if cmds[0] == "del": delLine()
        if cmds[0] == "add": addLine(cmds[1:]) # cmds[1:] = tail of cmds
        if cmds[0] == "dilate": dilate(cmds[1])
        if cmds[0] == "shear": shear(cmds[1], cmds[2])
        if cmds[0] == "stretch": stretch(cmds[1], cmds[2])
        if cmds[0] == "reflect": reflect(cmds[1])
    except IndexError:
        print("\nPlease input the correct number of parameters!")
    except ValueError:
        print("\nPlease input valid values!")
    
cmd = ""
def keyPressed(*args):
    global rquad, cmd
    chr = args[0].decode("utf-8")
    
    if args[0] == b'\x08':
        print(chr,end='',flush=True)
        print(' ',end='',flush=True)
        cmd = cmd[:-1]
    elif args[0] != b'\r':
        cmd = cmd + chr
    
    if (len(cmd) > 0):
        print(chr,end='',flush=True)
    else:
        print("\r>> ",end='',flush=True)
    
    if args[0] == b'\r':
        cmds = cmd.split(" ")
        doCmd(cmds)
        print("")
        cmd = ""
        print(">> ",end='',flush=True)

def main():
    global window
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1080, 720)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(b"Cube")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(1080, 720)
    glutMainLoop()
    
showCmds()
main()
