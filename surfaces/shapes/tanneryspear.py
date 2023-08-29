"""Tannery Spear."""
import numpy as np
from ..shapes import Shape


class TannerySpear(Shape):
    """The Tannery Spear shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.linspace(-2 * np.pi, 2 * np.pi, self.res)
        v = np.vstack(np.linspace(-np.pi, np.pi, self.res))
        a = 2

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""
            return a * np.sin(u) * np.cos(u) * np.cos(v)

        def fy(u, v):
            return a * np.sin(u) * np.cos(u) * np.sin(v)

        def fz(u):
            return 2 * np.sqrt(2 * a) * np.sin(u)

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y =np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(u), (self.res, self.res))

        return x, y, z
