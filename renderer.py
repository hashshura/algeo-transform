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
            "f": 0 # float, can be [x,y,z] for translation
        }
        
    def UpdatePoints(self):
        if self.updater["ctr"] < 60:
            self.updater["ctr"] += 1
            if self.updater["op"] == "dilate":
                self.shape.points = self.shape.points_before[:]
                f = str(1 + ((self.updater["f"] - 1)/60 * self.updater["ctr"]))
                self.shape.dilate(f)
            

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
        
        glColor3f(0,1,0)
        glVertex3f(2000,0,0)
        glVertex3f(-2000,0,0)

        glColor3f(1,0,0)
        glVertex3f(0,2000,0)
        glVertex3f(0,-200,0)

        glColor3f(0,0,1)
        glVertex3f(0,0,2000)
        glVertex3f(0,0,-2000)

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
        self.UpdatePoints()
    
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
        self.DrawAxes()
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
            
            if self.cmds[0] == "dilate":
                self.shape.points_before = self.shape.points[:]
                self.updater["op"] = "dilate"
                self.updater["ctr"] = 0
                self.updater["f"] = float(self.cmds[1])
            else:
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
        glutSpecialFunc(self.keySpecial)
        #InitGL(1080, 720)
        glutMainLoop()