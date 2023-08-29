"""Lamé."""
import numpy as np
from ..shapes import Shape


class Lame(Shape):
    """The Lamé shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.linspace(0, 2*np.pi, self.res)
        v = np.vstack(np.linspace(0, np.pi/2, self.res))
        a = 1
        b = 1
        c = 1
        fish = 1/2

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return np.sign(a) * np.cos(u)**(2 / fish) * np.cos(v)**(2 / fish)

        def fy(u, v):
            """Generate the y coordinate fron (u, v)."""

            return np.sign(b) * np.sin(u)**(2 / fish) * np.cos(v)**(2 / fish)

        def fz(v):
            """Generate the z coordinate fron (u, v)."""

            return np.sign(c) * np.sin(v)**(2 / fish)

        # Build the mesh grid while calculating the (x, y, z) coordinates.
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        z = np.broadcast_to(np.vectorize(fz)(v), (self.res, self.res))

        return x, y, z
