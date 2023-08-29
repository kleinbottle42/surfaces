"""Self intersecting disk."""
import numpy as np
from ..shapes import Shape


class SelfIntersectingDisk(Shape):
    """The Self Intersecting Disk shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.vstack(np.linspace(0, 2 * np.pi, self.res))
        v = np.linspace(0, 1, self.res)
        r = 1

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return r * v * np.cos(2 * u)

        def fy(u, v):
            return r * v * np.sin(2 * u)

        def fz(u, v):
            return r * v * np.cos(u)

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(u, v), (self.res, self.res))

        return x, y, z
