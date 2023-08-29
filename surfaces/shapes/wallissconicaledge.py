"""Wallis's Conical Edge."""
import numpy as np
from ..shapes import Shape


class WallissConicalEdge(Shape):
    """The Wallis's Conical Edge shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.linspace(-np.pi, np.pi, self.res) # I dont know the u and v values
        v = np.vstack(np.linspace(-1.0, 1.0, self.res))
        a = 1
        b = 1
        c = 1

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return v * np.cos(u)

        def fy(u, v):
            """Generate the y coordinate fron (u, v)."""

            return v * np.sin(u)


        def fz(u):
            return c * np.sqrt(a**2 - b**2 * (np.cos(u)**2))

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) data
        z = np.broadcast_to(np.vectorize(fz)(u), (self.res, self.res))

        return x, y, z
