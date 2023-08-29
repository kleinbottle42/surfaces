"""The catenoid surface."""
import numpy as np
from ..shapes import Shape


class CatalinsSurface(Shape):

    def calculate(self):
        """Calculate the shape coordinates."""

        res = self.res

        u = np.vstack(np.linspace(- np.pi, np.pi, res))
        v = np.linspace(-np.pi/2, np.pi/2 , res)

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return u - np.sin(u) * np.cosh(v)


        def fy(u, v):
            return 1 - np.cos(u) * np.cosh(v)

        def fz(u, v):
            return 4 * np.sin(u/2) * np.sinh(v/2)

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(u, v), (res, res))

        return x, y, z
