"""Torus."""
import numpy as np
from ..shapes import Shape


class Torus(Shape):
    """The Torus shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.vstack(np.linspace(-2 * np.pi, 2 * np.pi, self.res))
        v = np.linspace(-np.pi, np.pi, self.res)
        a = 4
        b = 2
        e = 0.9

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""
            return (a + b * np.cos(v)) * np.cos(u)

        def fy(u, v):
            return (a + b * np.cos(v)) * np.sin(u)

        def fz(v):
            return b * np.sin(v)

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y =np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(v), (self.res, self.res))

        return x, y, z
