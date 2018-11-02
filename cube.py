from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

Z_TRANSLATE = -2000.0 # To translate into viewport

window = 0
points = []
points_backup = []

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
    
def addPoint(point):
    global points, points_backup
    newpoint = []
    newpoint = newpoint + [float(point[0])]
    newpoint = newpoint + [float(point[1])]
    try:
        newpoint = newpoint + [float(point[2])]
    except IndexError:
        newpoint = newpoint + [0]
    
    points = points + [newpoint]
    points_backup = points[:]

def delPoint():
    global points, points_backup
    points = points[:-1]
    points_backup = points[:]

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
    global points
    value = float(value)
    newpoints = []
    for point in points:
        num = point[:]
        if (param == 'x'):
            num[0] += value*num[1] + value*num[2]
        if (param == 'y'):
            num[1] += value*num[0] + value*num[2]
        if (param == 'z'):
            num[2] += value*num[0] + value*num[1]
        newpoints += [[num[0], num[1], num[2]]]
    points = newpoints
    
def custom(matrix):
    global points
    newpoints = []
    try:
        _ = float(matrix[4])
        for point in points:
            newpoint = []
            newpoint += [point[0]*float(matrix[0]) + point[1]*float(matrix[1]) + point[2]*float(matrix[2])]
            newpoint += [point[0]*float(matrix[3]) + point[1]*float(matrix[4]) + point[2]*float(matrix[5])]
            newpoint += [point[0]*float(matrix[6]) + point[1]*float(matrix[7]) + point[2]*float(matrix[8])]
            newpoints += [newpoint]
        points = newpoints
    except IndexError:
        for point in points:
            newpoint = []
            newpoint += [point[0]*float(matrix[0]) + point[1]*float(matrix[1])]
            newpoint += [point[0]*float(matrix[2]) + point[1]*float(matrix[3])]
            newpoint += [0.0]
            newpoints += [newpoint]
        points = newpoints

def reset():
    global points, points_backup
    points = points_backup[:]

def doCmd(cmds):
    #cmds[0] = kata pertama
    #cmds[1] = kata kedua, dst
    try:
        if cmds[0] == "exit": exit()
        if cmds[0] == "stop": exit()
        if cmds[0] == "quit": exit()
        if cmds[0] == "del": delPoint()
        if cmds[0] == "add": addPoint(cmds[1:]) # cmds[1:] = tail of cmds
        if cmds[0] == "dilate": dilate(cmds[1])
        if cmds[0] == "shear": shear(cmds[1], cmds[2])
        if cmds[0] == "custom": custom(cmds[1:])
        if cmds[0] == "reset": reset()
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
