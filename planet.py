import math

G = 6.67*(10**(-11))
M_CENTRE = 3*(10**(30))


class Planet:
    def __init__(self,name, pos, v, a):
        self.name = name
        self.pos = pos
        self.d = math.sqrt(pos[0]**2 + pos[1]**2)
        self.v = v
        self.a = a

    def update_pos(self, t):
        x0 = self.pos[0]
        y0 = self.pos[1]
        v0x = self.v[0]
        v0y = self.v[1]
        a0x = self.a[0]
        a0y = self.a[1]
        x = x0 + v0x*t + (1/2)*a0x*(t**2)
        y = y0 + v0y*t + (1/2)*a0y*(t**2)
        self.pos = (x,y)
        self.d = math.sqrt(self.pos[0]**2 + self.pos[1]**2)

    def update_v(self, t):
        new_v = (self.v[0] + t*self.a[0], self.v[1] + t*self.a[1])
        self.v = new_v

    def update_a(self):
        a_magn = (G*M_CENTRE)/((self.d)**2)

        x1 = self.pos[0]
        y1 = self.pos[1]

        # Position of the central mass in chosen coordinate system:
        x2 = 0
        y2 = 0
        m = (y2 - y1)/(x2 - x1)

        if x1>0:
            b = (-1,-m)
        else:
            b = (1, m)
        b_magn = math.sqrt(1 + m**2)

        coeff = a_magn/b_magn

        a = (b[0]*coeff, b[1]*coeff)
        self.a = a

    def update_all(self, t):
        #Update planet position after some time t (in s)
        self.update_pos(t)

        #Update planet velocity after some time t (in s)
        self.update_v(t)

        #Update planet acceleration according to its position
        #relative to the central mass
        self.update_a()





