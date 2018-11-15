import math

TRANSFORM_CMDS = [
    "dilate",
    "shear",
    "custom",
    "stretch",
    "reflect",
    "translate",
    "rotate"
]

class Shape:
    
    def __init__(self):
        self.points = []
        self.points_backup = []
        self.points_before = []
        
    def addPoint(self, point):
        newpoint = []
        newpoint = newpoint + [float(point[0])]
        newpoint = newpoint + [float(point[1])]
        try:
            newpoint = newpoint + [float(point[2])]
        except IndexError:
            newpoint = newpoint + [0]
        
        self.points = self.points + [newpoint]
        self.points_backup = self.points[:]

    def delPoint(self):
        self.points = self.points[:-1]
        self.points_backup = self.points[:]

    def dilate(self, multiplier):
        newpoints = []
        for point in self.points:
            newpoint = []
            for number in point:
                newpoint += [number * float(multiplier)]
            newpoints += [newpoint]
        self.points = newpoints
        
    def shear(self, param, value):
        value = float(value)
        newpoints = []
        for point in self.points:
            num = point[:]
            if (param == 'x'):
                num[0] += value*num[1] + value*num[2]
            elif (param == 'y'):
                num[1] += value*num[0] + value*num[2]
            elif (param == 'z'):
                num[2] += value*num[0] + value*num[1]
            newpoints += [[num[0], num[1], num[2]]]
        self.points = newpoints
        
    def custom(self, matrix):
        newpoints = []
        try:
            _ = float(matrix[4])
            for point in self.points:
                newpoint = []
                newpoint += [point[0]*float(matrix[0]) + point[1]*float(matrix[1]) + point[2]*float(matrix[2])]
                newpoint += [point[0]*float(matrix[3]) + point[1]*float(matrix[4]) + point[2]*float(matrix[5])]
                newpoint += [point[0]*float(matrix[6]) + point[1]*float(matrix[7]) + point[2]*float(matrix[8])]
                newpoints += [newpoint]
            self.points = newpoints
        except IndexError:
            for point in self.points:
                newpoint = []
                newpoint += [point[0]*float(matrix[0]) + point[1]*float(matrix[1])]
                newpoint += [point[0]*float(matrix[2]) + point[1]*float(matrix[3])]
                newpoint += [0.0]
                newpoints += [newpoint]
            self.points = newpoints

    def reset(self):
        self.points = self.points_backup[:]

    def stretch(self, param, value):
        value = float(value)
        newpoints = []
        for point in self.points:
            num = point[:]
            if (param == 'x'):
                num[0] = num[0]*value
            if (param == 'y'):
                num[1] = num[1]*value
            if (param == 'z'):
                num[2] =num[2]*value
            newpoints += [[num[0], num[1], num[2]]]
        self.points = newpoints

    def reflect(self, param):
        newpoints = []
        if (param[0] == '('):
            param = ''.join(param[1:-1]).split(',')
        for point in self.points:
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
            elif (param == "xy") or (param == "yx"):
                num[2] = -num[2]
            elif (param == "xz") or (param == "zx"):
                num[1] = -num[1]
            elif (param == "yz") or (param == "zy"):
                num[0] = -num[0]
            else:
                num[0] = float(param[0])*2 - num[0]
                num[1] = float(param[1])*2 - num[1]
                num[2] = float(param[2])*2 - num[2]
            newpoints += [num]
        self.points = newpoints

    def translate(self, delta):
        dx = float(delta[0])
        dy = float(delta[1])
        try:
            dz = float(delta[2])
        except IndexError:
            dz = 0.0
        newpoints = []
        for point in self.points:
            newpoint = point[:]
            newpoint[0] = point[0] + dx
            newpoint[1] = point[1] + dy
            newpoint[2] = point[2] + dz
            newpoints += [newpoint]
        self.points = newpoints

    def rotate(self, deg, param, titikpusat):
        deg = float(deg)
        a = float(titikpusat[0])
        b = float(titikpusat[1])
        try:
            c = float(titikpusat[2])
        except IndexError:
            c = 0.0
        rad = math.radians(deg)
        newpoints = []
        for point in self.points:
            newpoint = point[:]
            if (param == 'x'):
                newpoint[0] = point[0]
                newpoint[1] = b + (point[1] - b)*math.cos(rad) - (point[2] - c)*math.sin(rad)
                newpoint[2] = c + (point[1] - b)*math.sin(rad) + (point[2] - c)*math.cos(rad)
            elif (param == 'y'):
                newpoint[0] = a + (point[0] - a)*math.cos(rad) + (point[2] - c)*math.sin(rad)
                newpoint[1] = point[1]
                newpoint[2] = c + -1*(point[0] - a)*math.sin(rad) + (point[1] - b)*math.cos(rad)
            elif (param == 'z'):
                newpoint[0] = a + (point[0] - a)*math.cos(rad) - (point[1] - b)*math.sin(rad)
                newpoint[1] = b + (point[0] - a)*math.sin(rad) + (point[1] - b)*math.cos(rad)
                newpoint[2] = point[2]
            newpoints += [newpoint]
        self.points = newpoints
        
    def help(self,command):
        print("================================???? HELPER ????================================")
        print()
        if (command == "dilate") or (command == "Dilate"):
            print(" Type \"dilate v\" to scale the polygon (v = float)")
        elif (command == "shear") or (command == "Shear"):
            print(" for 2D")
            print(" Type \"shear p v\" to shear the polygon (p = x/y) (v = float)")
            print(" for 3D")
            print(" Type \"shear p v\" to shear the polygon (p = x/y/z) (v = float)")
        elif (command == "stretch") or (command == "Stretch"):
            print(" for 2D")
            print(" Type \"stretch p v\" to stretch the polygon (p = x/y) (v = float)")
            print(" for 3D")
            print(" Type \"stretch p v\" to stretch the polygon (p = x/y/z) (v = float)")
        elif (command == "reflect") or (command == "Reflect"):
            print(" Type \"reflect p\" to reflect the polygon (p = x/x=-y/etc)")
        elif (command == "translate") or (command == "Translate"):
            print(" for 2D")
            print(" Type \"translate dx dy\" to translate the polygon (dx,dy = float)")
            print(" for 3D")
            print(" Type \"translate dx dy dz\" to translate the polygon (dx,dy,dz = float)")
        elif (command == "rotate") or (command == "Rotate"):
            print(" for 2D")
            print(" Type \"rotate r a b\" to rotate the polygon (r = float) (a,b = central point)")
            print(" for 3D")
            print(" Type \"rotate r p a b c\" to rotate the polygon (r = float) (p = x/y/z) (a,b,c = central point)")
        elif (command == "custom") or (command == "Custom"):
            print(" for 2D")
            print(" Type \"custom a b c d\" to execute custom transformation matrix (a,b,c,d is a 2x2 matrix)")
            print(" for 3D")
            print(" Type \"custom a b c d e f g h i\" to execute custom transformation matrix (a-i is a 3x3 matrix")
        else:
            print(" Command not found!")
            print(" Please type \"help <command's name>\"")
            print(" Command's List:")
            print(" -dilate")
            print(" -shear")
            print(" -stretch")
            print(" -reflect")
            print(" -translate")
            print(" -rotate")
            print(" -custom")
        print()
        print("================================================================================")
    
    def doCmd(self, renderer):
        #cmds[0] = kata pertama
        #cmds[1] = kata kedua, dst
        cmds = renderer.cmds
        try:
            self.points_before = self.points[:]
            renderer.updater["op"] = cmds[0]
            if cmds[0] in TRANSFORM_CMDS:
                renderer.updater["deltas"] = []
                renderer.updater["ctr"] = 0
                s = Shape()
                s.points = self.points[:]
                if cmds[0] == "rotate":
                    renderer.updater["ctr"] = 0
                    renderer.updater["f"] = float(cmds[1])
                    try:
                        # 2D
                        renderer.updater["a"] = "z"
                        renderer.updater["f1"] = float(cmds[2])
                        renderer.updater["f2"] = float(cmds[3])
                        renderer.updater["f3"] = 0.0
                    except ValueError:
                        # 3D
                        renderer.updater["a"] = cmds[2]
                        renderer.updater["f1"] = float(cmds[3])
                        renderer.updater["f2"] = float(cmds[4])
                        renderer.updater["f3"] = float(cmds[5])
                elif cmds[0] == "dilate": s.dilate(cmds[1])
                elif cmds[0] == "shear": s.shear(cmds[1], cmds[2])
                elif cmds[0] == "stretch": s.stretch(cmds[1], cmds[2])
                elif cmds[0] == "reflect": s.reflect(cmds[1])
                elif cmds[0] == "translate": s.translate(cmds[1:])
                elif cmds[0] == "custom": s.shear(cmds[1:])
                if cmds[0] != "rotate":
                    for b,a in zip(self.points, s.points):
                        delta_point = a[:]
                        delta_point[0] -= b[0]
                        delta_point[1] -= b[1]
                        delta_point[2] -= b[2]
                        renderer.updater["deltas"] += [delta_point]
            
            elif cmds[0] == "exit": exit()
            elif cmds[0] == "stop": exit()
            elif cmds[0] == "quit": exit()
            elif cmds[0] == "del": self.delPoint()
            elif cmds[0] == "add": self.addPoint(cmds[1:])
            elif cmds[0] == "reset": self.reset()
            elif cmds[0] == "help": self.help(cmds[1])
            elif (cmds[0] == "A") or (cmds[0] == "a"): renderer.toggleAxes = (renderer.toggleAxes+1)%2
            else: print("\nCommand not found.")
        except IndexError:
            print("\nPlease input the correct number of parameters.")
            renderer.updater["ctr"] = 1e9
        except ValueError:
            print("\nPlease input valid values.")
            renderer.updater["ctr"] = 1e9
