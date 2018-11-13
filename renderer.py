from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

# To translate into viewport perspective
Z_PERSPECTIVE_TR = -2000.0

class Renderer:

    def __init__(self, shape, dimension):
        
        self.shape = shape
        self.dimension = dimension
        
        self.window = 0
        self.dim = 3.0
        self.toggleAxes = 1
        self.toggleValues = 1
        self.toggleMode = 0
        self.th = 0.0
        self.ph = 0.0
        self.fov = 55
        self.cmd = ""
        
        self.updater = {
            "ctr": 60,
            "op": "",
            "a": "", # axis
            "f": 0, # float
            "f1": 0, # could be for xyz
            "f2": 0,
            "f3": 0
        }
        
    def Animate(self):
        if self.updater["ctr"] < 60:
            self.updater["ctr"] += 1
            if self.updater["op"] == "dilate":
                self.shape.points = self.shape.points_before[:]
                f = 1 + ((self.updater["f"] - 1)/60 * self.updater["ctr"])
<<<<<<< HEAD
                self.shape.dilate(f1)
=======
                self.shape.dilate(f)
>>>>>>> fa11711d339607761d2aaf3ae71d51bb0990d9c1
            elif self.updater["op"] == "translate":
                self.shape.points = self.shape.points_before[:]
                f1 = self.updater["f1"]/60 * self.updater["ctr"]
                f2 = self.updater["f2"]/60 * self.updater["ctr"]
                f3 = self.updater["f3"]/60 * self.updater["ctr"]
                self.shape.translate([f1, f2, f3])
            elif self.updater["op"] == "rotate":
                self.shape.points = self.shape.points_before[:]
                f = self.updater["f"]/60 * self.updater["ctr"]
                a = self.updater["a"]
                f1 = self.updater["f1"]
                f2 = self.updater["f2"]
                f3 = self.updater["f3"]
                self.shape.rotate(f, a, [f1, f2, f3])
            elif self.updater["op"] == "shear":
                self.shape.points = self.shape.points_before[:]
                f = self.updater["f"]/60 * self.updater["ctr"]
                a = self.updater["a"]
                self.shape.shear(a, f)
            elif self.updater["op"] == "stretch":
                self.shape.points = self.shape.points_before[:]
                f = 1 + ((self.updater["f"] - 1)/60 * self.updater["ctr"])
                a = self.updater["a"]
                self.shape.stretch(a, f)

    def InitGL(self, Width, Height):
        glClearColor(1, 1, 1, 0.0)
        glClearDepth(1.0)            
        glDepthFunc(GL_LESS)          
        glEnable(GL_DEPTH_TEST)
        glPolygonMode(GL_FRONT, GL_FILL)    
        glPolygonMode(GL_BACK, GL_FILL)     
        glShadeModel(GL_SMOOTH)           
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if (self.toggleMode):                   
            gluPerspective(self.fov,float(Width)/float(Height), self.dim/4, 2*Z_PERSPECTIVE_TR)
        else:
            specialhere = self.dim*300
            glOrtho(-specialhere*float(Width)/float(Height), +specialhere*float(Width)/float(Height),-specialhere,+specialhere, -specialhere, +specialhere)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def ReSizeGLScene(self, Width, Height):
        if Height == 0:                     
            Height = 1

        glViewport(0, 0, Width, Height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, float(Width)/float(Height), 0.1, 2 * Z_PERSPECTIVE_TR)
        glMatrixMode(GL_MODELVIEW)

    def DrawAxes(self):
        #Draw XY Cartesian Area
        glBegin(GL_LINES)
<<<<<<< HEAD
        for i in range(-40,40):
            #XY
            if (self.dimension == "2D"):    
                glColor3f(0.7,0.7,0.7)
                if (i != 0):
                    if (i%5 == 0):
                        glColor3f(0,0,0)
                    glVertex3f(2000,i*50,0)
                    glVertex3f(-2000,i*50,0)
                if (i != 0):
                    if (i%5 == 0):
                        glColor3f(0,0,0)
                    glVertex3f(i*50,-2000,0)
                    glVertex3f(i*50,2000,0)
            #XZ
            if (self.dimension == "3D"):
                if (i != 0):
                    if (i%5 == 0):
                        glColor3f(0,0,0)
                    glVertex3f(2000,0,i*50)
                    glVertex3f(-2000,0,i*50)
                if (i != 0):
                    if (i%5 == 0):
                        glColor3f(0,0,0)
                    glVertex3f(i*50,0,-2000)
                    glVertex3f(i*50,0,2000)
            #YZ
            '''
=======
        
        for i in range(-40,40):
            #XY    
            glColor3f(0.7,0.7,0.7)
            if (i != 0):
                if (i%5 == 0):
                    glColor3f(0,0,0)
                glVertex3f(2000,i*50,0)
                glVertex3f(-2000,i*50,0)
            if (i != 0):
                if (i%5 == 0):
                    glColor3f(0,0,0)
                glVertex3f(i*50,-2000,0)
                glVertex3f(i*50,2000,0)
            #XZ
            if (i != 0):
                if (i%5 == 0):
                    glColor3f(0,0,0)
                glVertex3f(2000,0,i*50)
                glVertex3f(-2000,0,i*50)
            if (i != 0):
                if (i%5 == 0):
                    glColor3f(0,0,0)
                glVertex3f(i*50,0,-2000)
                glVertex3f(i*50,0,2000)
            #YZ
>>>>>>> fa11711d339607761d2aaf3ae71d51bb0990d9c1
            if (i != 0):
                if (i%5 == 0):
                    glColor3f(0,0,0)
                glVertex3f(0,2000,i*50)
                glVertex3f(0,-2000,i*50)
            if (i != 0):
                if (i%5 == 0):
                    glColor3f(0,0,0)
                glVertex3f(0,i*50,-2000)
                glVertex3f(0,i*50,2000)
<<<<<<< HEAD
            '''
=======
        
>>>>>>> fa11711d339607761d2aaf3ae71d51bb0990d9c1
        glColor3f(0,1,0)
        glVertex3f(2000,0,0)
        glVertex3f(-2000,0,0)

        glColor3f(1,0,0)
        glVertex3f(0,2000,0)
<<<<<<< HEAD
        glVertex3f(0,-2000,0)

        if (self.dimension == "3D"):
            glColor3f(0,0,1)
            glVertex3f(0,0,2000)
            glVertex3f(0,0,-2000)
=======
        glVertex3f(0,-200,0)

        glColor3f(0,0,1)
        glVertex3f(0,0,2000)
        glVertex3f(0,0,-2000)

>>>>>>> fa11711d339607761d2aaf3ae71d51bb0990d9c1
        glEnd()

    def DrawPolygon(self):
        glBegin(GL_POLYGON)
        for point in self.shape.points:
            glColor3f(0.4,0.4,1)
            glVertex3f(point[0], point[1], point[2])
        glEnd()

    def Sample3DModel(self):
        glBegin(GL_QUADS)                 
        #Sisi 1
        glColor3f(0,1,0)            
        glVertex3f(self.shape.points[0][0],self.shape.points[0][1],self.shape.points[0][2])        
        glVertex3f(self.shape.points[1][0],self.shape.points[1][1],self.shape.points[1][2])
        glVertex3f(self.shape.points[3][0],self.shape.points[3][1],self.shape.points[3][2])
        glVertex3f(self.shape.points[2][0],self.shape.points[2][1],self.shape.points[2][2])

        #Sisi 2
        glColor3f(1,0,0)            
        glVertex3f(self.shape.points[0][0],self.shape.points[0][1],self.shape.points[0][2])        
        glVertex3f(self.shape.points[1][0],self.shape.points[1][1],self.shape.points[1][2])
        glVertex3f(self.shape.points[5][0],self.shape.points[5][1],self.shape.points[5][2])
        glVertex3f(self.shape.points[4][0],self.shape.points[4][1],self.shape.points[4][2])

        #Sisi 3
        glColor3f(0,0,1)            
        glVertex3f(self.shape.points[0][0],self.shape.points[0][1],self.shape.points[0][2])        
        glVertex3f(self.shape.points[2][0],self.shape.points[2][1],self.shape.points[2][2])
        glVertex3f(self.shape.points[6][0],self.shape.points[6][1],self.shape.points[6][2])
        glVertex3f(self.shape.points[4][0],self.shape.points[4][1],self.shape.points[4][2])

        #Sisi 4
        glColor3f(1,1,0)            
        glVertex3f(self.shape.points[2][0],self.shape.points[2][1],self.shape.points[2][2])        
        glVertex3f(self.shape.points[3][0],self.shape.points[3][1],self.shape.points[3][2])
        glVertex3f(self.shape.points[7][0],self.shape.points[7][1],self.shape.points[7][2])
        glVertex3f(self.shape.points[6][0],self.shape.points[6][1],self.shape.points[6][2])

        #Sisi 5
        glColor3f(0,1,1)            
        glVertex3f(self.shape.points[4][0],self.shape.points[4][1],self.shape.points[4][2])        
        glVertex3f(self.shape.points[5][0],self.shape.points[5][1],self.shape.points[5][2])
        glVertex3f(self.shape.points[7][0],self.shape.points[7][1],self.shape.points[7][2])
        glVertex3f(self.shape.points[6][0],self.shape.points[6][1],self.shape.points[6][2])

        #Sisi 6
        glColor3f(1,0,1)            
        glVertex3f(self.shape.points[1][0],self.shape.points[1][1],self.shape.points[1][2])        
        glVertex3f(self.shape.points[3][0],self.shape.points[3][1],self.shape.points[3][2])
        glVertex3f(self.shape.points[7][0],self.shape.points[7][1],self.shape.points[7][2])
        glVertex3f(self.shape.points[5][0],self.shape.points[5][1],self.shape.points[5][2])  
        glEnd()                                   

    def DrawGLScene(self):
        self.Animate()
    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   
        glEnable(GL_DEPTH_TEST) 

        glLoadIdentity()
        
        if (self.toggleMode):
            Ex = -2*self.dim*math.sin(self.th)*math.cos(self.ph)
            Ey = +(2*self.dim*math.sin(self.ph))
            Ez = +(2*self.dim*math.sin(self.th)*math.cos(self.ph))
            gluLookAt(Ex,Ey,Ez , 0,0,0 , 0,math.cos(self.ph),0)
        else:
            glRotatef(self.ph,1,0,0)
            glRotatef(self.th,0,1,0)
            
        if (self.dimension == "2D"):
            self.DrawPolygon()
        elif (self.dimension == "3D"):
            self.Sample3DModel()
<<<<<<< HEAD
        self.DrawAxes()
=======
        if (self.toggleAxes == 1):
            self.DrawAxes()
>>>>>>> fa11711d339607761d2aaf3ae71d51bb0990d9c1
        self.InitGL(1080,720)
        glutPostRedisplay()
        
        glFlush()
        glutSwapBuffers()

    def keyPressed(self, *args):
        chr = args[0].decode("utf-8")

        if args[0] == b'\x08':
            print(chr,end='',flush=True)
            print(' ',end='',flush=True)
            self.cmd = self.cmd[:-1]
        elif args[0] != b'\r':
            self.cmd = self.cmd + chr
        
        if (len(self.cmd) > 0):
            print(chr,end='',flush=True)
        else:
            print("\r>> ",end='',flush=True)
        
        if args[0] == b'\r':
            self.cmds = self.cmd.split(" ")
            self.shape.doCmd(self)
            
            print("")
            self.cmd = ""
            print(">> ",end='',flush=True)

        self.InitGL(1080,720)
        glutPostRedisplay()

    def keySpecial(self, key, x, y):
        if (key == GLUT_KEY_RIGHT): self.th += 5
        elif (key == GLUT_KEY_LEFT): self.th -= 5
        elif (key == GLUT_KEY_UP): self.ph += 5
        elif (key == GLUT_KEY_DOWN): self.ph -= 5

        self.th = self.th%360
        self.ph = self.ph%360

        self.InitGL(1080,720)
        glutPostRedisplay()
        
    def render(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(1080, 720)
        #glutInitself.windowPosition(0, 0)
        self.window = glutCreateWindow(b"Tugas Besar Aljabar Geometri 2")

        glutDisplayFunc(self.DrawGLScene)
        glutIdleFunc(self.DrawGLScene)
        glutReshapeFunc(self.ReSizeGLScene)
        glutKeyboardFunc(self.keyPressed)
<<<<<<< HEAD
        if (self.dimension == "3D"):
            glutSpecialFunc(self.keySpecial)
=======
        glutSpecialFunc(self.keySpecial)
        #InitGL(1080, 720)
>>>>>>> fa11711d339607761d2aaf3ae71d51bb0990d9c1
        glutMainLoop()