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
'''
def Sample3DModel():
    global points

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()
    glTranslatef(0.0,0.0,Z_TRANSLATE) 
    glBegin(GL_QUADS)                 

    points = [[100,100,100],[100,100,-100],[100,-100,100],[100,-100,-100],[-100,100,100],[-100,100,-100],[-100,-100,100],[-100,-100,-100]]

    #Sisi 1
    glColor3f(0,1,0)            
    glVertex3f(points[0][0],points[0][1],points[0][2])        
    glVertex3f(points[1][0],points[1][1],points[1][2])
    glVertex3f(points[3][0],points[3][1],points[3][2])
    glVertex3f(points[2][0],points[2][1],points[2][2])

    #Sisi 2
    glColor3f(0,1,0)            
    glVertex3f(points[0][0],points[0][1],points[0][2])        
    glVertex3f(points[1][0],points[1][1],points[1][2])
    glVertex3f(points[5][0],points[5][1],points[5][2])
    glVertex3f(points[4][0],points[4][1],points[4][2])

    #Sisi 3
    glColor3f(0,1,0)            
    glVertex3f(points[0][0],points[0][1],points[0][2])        
    glVertex3f(points[2][0],points[2][1],points[2][2])
    glVertex3f(points[6][0],points[6][1],points[6][2])
    glVertex3f(points[4][0],points[4][1],points[4][2])

    #Sisi 4
    glColor3f(0,1,0)            
    glVertex3f(points[2][0],points[2][1],points[2][2])        
    glVertex3f(points[3][0],points[3][1],points[3][2])
    glVertex3f(points[6][0],points[6][1],points[6][2])
    glVertex3f(points[7][0],points[7][1],points[7][2])

    #Sisi 5
    glColor3f(0,1,0)            
    glVertex3f(points[4][0],points[4][1],points[4][2])        
    glVertex3f(points[5][0],points[5][1],points[5][2])
    glVertex3f(points[7][0],points[7][1],points[7][2])
    glVertex3f(points[6][0],points[6][1],points[6][2])

    #Sisi 6
    glColor3f(0,1,0)            
    glVertex3f(points[1][0],points[1][1],points[1][2])        
    glVertex3f(points[3][0],points[3][1],points[3][2])
    glVertex3f(points[7][0],points[7][1],points[7][2])
    glVertex3f(points[5][0],points[5][1],points[5][2])  
    glEnd()                                        
    glutSwapBuffers()
'''
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
    print("Type \"reset\" to reset any operations done after adding or deleting a point")
    print("Type \"dilate v\" to scale the polygon (v = float)")
    print("Type \"shear p v\" to shear the polygon (p = x/y/z) (v = float)")
    print("Type \"stretch p v\" to stretch the polygon (p = x/y/z) (v = float)")
    print("Type \"reflect p\" to reflect the polygon (p = x/x=-y/etc)")
    print("Type \"translate dx dy dz\" to translate the polygon (dx,dy,dz = float)")
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

def stretch(param, value):
    value = float(value)
    global points
    newpoints = []
    for point in points:
        num = point[:]
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
    if (param[0] == '('):
        param = ''.join(param[1:-1]).split(',')
    for point in points:
        num = point[:]
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
            num[0] = float(param[0])*2 - num[0]
            num[1] = float(param[1])*2 - num[1]
            num[2] = float(param[2])*2 - num[2]
        newpoints += [[num[0], num[1], num[2]]]
    points = newpoints

def translate(delta):
    dx = float(delta[0])
    dy = float(delta[1])
    try:
        dz = float(delta[2])
    except IndexError:
        dz = 0.0
    global points
    newpoints = []
    for point in points:
        newpoint = point[:]
        newpoint[0] = point[0] + dx
        newpoint[1] = point[1] + dy
        newpoint[2] = point[2] + dz
        newpoints += [newpoint]
    points = newpoints
    
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
        if cmds[0] == "stretch": stretch(cmds[1], cmds[2])
        if cmds[0] == "reflect": reflect(cmds[1])
        if cmds[0] == "translate": translate(cmds[1:])
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
