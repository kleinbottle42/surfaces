import numpy as np
from ..shapes import Shape


class GabrielsTrumpet(Shape):
    """The Catenoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        res = self.res

        u = np.linspace(-np.pi, np.pi, res)
        v = np.vstack(np.linspace(-np.pi, np.pi, res))
        a = 2

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""
            return a * u * np.cos(v)

        def fy(u, v):
            return a * u * np.sin(v)


        def fz(u):
            return a / u


        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(u), (res, res))

        

        return x, y, z