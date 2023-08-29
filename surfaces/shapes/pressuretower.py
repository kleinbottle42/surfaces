"""Pressure Tower."""
import numpy as np
from ..shapes import Shape


class PressureTower(Shape):
    """The Pressure Tower shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.linspace(-np.pi, np.pi, self.res)
        v = np.vstack(np.linspace(-np.pi, np.pi, self.res))
        a = 1
        k = 1

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""
            return a * np.exp(k * u) * np.cos(v)

        def fy(u, v):
            return a * np.exp(k * u) * np.sin(v)

        def fz(u, v):
            return a * u

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(u, v), (self.res, self.res))

        return x, y, z
