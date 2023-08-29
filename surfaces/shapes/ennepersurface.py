import numpy as np
from ..shapes import Shape


class EnneperSurface(Shape):
    """The Catenoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        res = self.res

        u = np.vstack(np.linspace(-10, 10, res))
        v = np.linspace(-10, 10 , res)

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return 1/3 * u *(1 - 1/3 * u**2 + v**2)


        def fy(u, v):
            return 1/3 * v *(1 - 1/3 * v**2 + u**2)

        def fz(u, v):
            return 1/3 *(u**2 - v**2)

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(u, v), (res, res))

        

        return x, y, z