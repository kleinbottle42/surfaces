"""Plücker's Conoid."""
import numpy as np
from ..shapes import Shape


class PluckersConoid(Shape):
    """The Plücker's Conoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.linspace(-np.pi, np.pi, self.res)
        v = np.vstack(np.linspace(0 , 1 , self.res))
        n = 2

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return v * np.cos(u)

        def fy(u, v):
            """Generate the y coordinate fron (u, v)."""

            return v * np. sin(u)

        def fz(u):
            return np.sin(n * u)

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(u), (self.res, self.res))

        return x, y, z
