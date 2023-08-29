import numpy as np
from ..shapes import Shape


class CrosscappedDisk(Shape):
    """The Catenoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        res = self.res

        u = np.vstack(np.linspace(0, 2 * np.pi, res))
        v = np.linspace(0, 2 * np.pi, res)
        r = 1

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return r * (1 + np.cos(v)) * np.cos(u)


        def fy(u, v):
            return r * (1 + np.cos(v)) * np.sin(u)

        def fz(u, v):
            return -np.tanh(u - np.pi) * r * np.sin(v)

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(u, v), (res, res))

        return x, y, z