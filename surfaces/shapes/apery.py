"""Apery."""
import numpy as np
from ..shapes import Shape


class Apery(Shape):
    """The Apery shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.linspace(0, 1, self.res)
        v = np.linspace(0, 2 * np.pi, self.res)
        w = np.vstack(np.linspace(0, 2 * np.pi, self.res))
        a = 1

        def fx(u, v, w):
            """Generate the x coordinate fron (u, v)."""

            return a/2 * ((3 * u**2 - 1) + 2 * v * w * (v**2 - w**2) + u * w * (u**2 - w**2) + u * v * (v**2 - u**2))

        def fy(u, v, w):
            """Generate the y coordinate fron (u, v)."""

            return (a * np.sqrt(3))/2 * ((v**2 - w**2) + u * v * (w**2 - u**2) + u * v * (v**2 - u**2))

        def fz(u, v, w):
            """Generate the z coordinate fron (u, v)."""

            return a * (u + v + w) * ((u + v + w)**3 - 4 * (u - v) * (v - w) * (w - u))

        # Build the mesh grid while calculating the (x, y, z) coordinates.
        x = np.vectorize(fx)(u, v, w)
        y = np.vectorize(fy)(u, v, w)
        z = np.broadcast_to(np.vectorize(fz)(u, v, w), (self.res, self.res))

        return x, y, z
