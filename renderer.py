from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

# To translate into viewport perspective
Z_PERSPECTIVE_TR = -2000.0
ANIMATION_DURATION = 1

class Renderer:

    def __init__(self, shape, dimension):
        
        self.shape = shape
        self.dimension = dimension
        
        self.window = 0
        self.dim = 3.0
        self.toggleAxes = 1
        self.th = 45.0
        self.ph = 30.0
        self.cmd = ""
        
        self.updater = {
            "ctr": 1e9,
            "op": "",
            "a": "", # axis
            "f": 0, # float
            "f1": 0, # could be for xyz
            "f2": 0,
            "f3": 0,
            "deltas": []
        }
        
    def Animate(self):
        frames = 60 * ANIMATION_DURATION
        if self.updater["ctr"] < frames:
            self.updater["ctr"] += 1
            if self.updater["op"] == "rotate":
                self.shape.points = self.shape.points_before[:]
                f = self.updater["f"]/frames * self.updater["ctr"]
                a = self.updater["a"]
                f1 = self.updater["f1"]
                f2 = self.updater["f2"]
                f3 = self.updater["f3"]
                self.shape.rotate(f, a, [f1, f2, f3])
            else:
                self.shape.points = []
                it = 0
                for pt_d in self.updater["deltas"]:
                    pt = self.shape.points_before[it][:]
                    pt[0] += pt_d[0]/frames * self.updater["ctr"]
                    pt[1] += pt_d[1]/frames * self.updater["ctr"]
                    pt[2] += pt_d[2]/frames * self.updater["ctr"]
                    self.shape.points += [pt]
                    it += 1

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
        glLineWidth(1)
        glBegin(GL_LINES)
        #DrawGrid
        for i in range(-40,40):
            glColor3f(0.7,0.7,0.7)
            #XY    
            if (self.dimension == "2D"):
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
            '''
        glEnd()
        glLineWidth(3)
        glBegin(GL_LINES)
        glColor3f(0,1,0)
        glVertex3f(2000,0,0)
        glVertex3f(0,0,0)

        glColor3f(1,0,0)
        glVertex3f(0,2000,0)
        glVertex3f(0,0,0)

        if (self.dimension == "3D"):
            glColor3f(0,0,1)
            glVertex3f(0,0,2000)
            glVertex3f(0,0,0)
        glEnd()
        #Sumbu Negatif
        glLineStipple(5, 0xAAAA)
        glEnable(GL_LINE_STIPPLE)
        glBegin(GL_LINES)
        glColor3f(0,1,0)
        glVertex3f(-2000,0,0)
        glVertex3f(0,0,0)

        glColor3f(1,0,0)
        glVertex3f(0,-2000,0)
        glVertex3f(0,0,0)

        if(self.dimension == "3D"):
            glColor3f(0,0,1)
            glVertex3f(0,0,-2000)
            glVertex3f(0,0,0)
        glEnd()
        glDisable(GL_LINE_STIPPLE)

    def DrawPolygon(self):
        glBegin(GL_POLYGON)
        for point in self.shape.points:
            glColor3f(0,0,1)
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
        if (self.dimension == "2D"):
            self.ph = 0
            self.th = 0
        glRotatef(self.ph,1,0,0) # Change perspective
        glRotatef(self.th,0,1,0) # Change perspective
            
        if (self.dimension == "2D"):
            self.DrawPolygon()
        elif (self.dimension == "3D"):
            self.Sample3DModel()
        if (self.toggleAxes == 1):
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
            self.shape.doCmd(self)
            
            print("")
            self.cmd = ""
            print(">> ",end='',flush=True)

        self.InitGL(1080,720)
        glutPostRedisplay()

    def keySpecial(self, key, x, y):
        if (self.dimension == "3D"):
            if (key == GLUT_KEY_RIGHT): self.th += 5
            elif (key == GLUT_KEY_LEFT): self.th -= 5
            elif (key == GLUT_KEY_UP): self.ph += 5
            elif (key == GLUT_KEY_DOWN): self.ph -= 5
        if ((key == GLUT_KEY_PAGE_DOWN) and (self.dim > 1)): self.dim -= 0.25
        elif ((key == GLUT_KEY_PAGE_UP) and (self.dim < 7.5)): self.dim += 0.25
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
        glutMainLoop()