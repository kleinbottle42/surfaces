"""Sphere."""
import numpy as np
from ..shapes import Shape


class Sphere(Shape):
    """The sphere shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.linspace(-np.pi, np.pi, self.res)
        v = np.vstack(np.linspace(-np.pi / 2, np.pi / 2, self.res))
        R = 10

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""
            return R * np.cos(u) * np.cos(v)

        def fy(u, v):
            return R * np.sin(u) * np.cos(v)

        def fz(v):
            return R * np.sin(v)


        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u,v)
        y = np.vectorize(fy)(u,v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(v), (self.res, self.res))

        return x, y, z
