from typing import Tuple

class Physics:
    def __init__(self, pos, v, a, dt, m, g, rho, C, A):
        # pos   : position of the object
        # v     : velocity of the object
        # a     : acceleration of the object
        # dt    : delta time i. e. amount of time passed
        # m     : mass of the object
        # g     : gravitational acceleration
        # rho   : density of air
        # C     : drag coefficient of the object
        # A     : face area of the object

        self.position = pos
        self.pos = pos

        self.velocity = v
        self.v = v
        
        self.acceleration = a
        self.a = a

        self.deltatime = dt
        self.dt = dt

        self.mass = m
        self.m = m

        self.density = rho
        self.rho = rho

        self.drag_coeff = C
        self.C = C

        self.area = A
        self.A = A

    def getNewPosition(self) -> Tuple[int, int]:
        x = self.pos[0]
        y = self.pos[1]
        
        v = self.calculateVelocity()
        dt = self.dt

        return (x, y - v/dt)
    
    def getNewVelocity(self) -> float:
        v = self.v
        a = self.getNewAcceleration()
        dt = self.dt

        return v + a/dt

    def getNewAcceleration(self) -> float:
        G = self.getGravitationalForce()
        F = self.getNewDrag()
        m = self.m

        return (G - F) / m

    def getGravitationalForce(self) -> float:
        g = self.g
        m = self.m

        return g * m

    def getNewDrag(self) -> float:
        rho = self.rho
        C = self.C
        A = self.A
        v = self.v

        return rho * C * A * (v ** 2)

