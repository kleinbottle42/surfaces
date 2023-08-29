"""Sinus Surface."""
import numpy as np
from ..shapes import Shape


class SinusSurface(Shape):
    """The Sinus Surface shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.vstack(np.linspace(-2 * np.pi, 2 * np.pi, self.res))
        v = np.linspace(-np.pi, np.pi, self.res)
        a = 1

        def fx(u):
            """Generate the x coordinate fron (u, v)."""
            return a * np.sin(u)

        def fy(v):
            return a * np.sin(v)

        def fz(u, v):
            return a * np.sin(u + v)

        # Generate the coordinates based on the functions
        x = np.broadcast_to(np.vectorize(fx)(u), (self.res, self.res))
        y = np.broadcast_to(np.vectorize(fy)(v), (self.res, self.res))
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(u, v), (self.res, self.res))

        return x, y, z
