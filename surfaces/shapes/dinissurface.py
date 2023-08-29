import numpy as np
from ..shapes import Shape


class DinisSurface(Shape):
    """The Catenoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        res = self.res

        u = np.vstack(np.linspace(0, 4 * np.pi, res))
        v = np.linspace(0.01, 1, res)
        a = 1
        b = .2

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return a * np.cos(u) * np.sin(v) 


        def fy(u, v):
            return a * np.sin(u) * np.sin(v) 

        def fz(u, v):
            return a * (np.cos (v) + np.log([np.tan(v/2)])) + b * u

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(u, v), (res, res))

        return x, y, z