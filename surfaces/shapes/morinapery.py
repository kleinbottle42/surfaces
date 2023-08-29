"""Morin Apery."""
import numpy as np
from ..shapes import Shape


class MorinApery(Shape):
    """The MorinApery shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.linspace(0, 1, self.res)
        v = np.vstack(np.linspace(0, 2 * np.pi, self.res))
        k = 1
        K = np.cos(u) / (np.sqrt(2) - k * np.sin(2 * u) * np.sin(3 * v))


        def fx(u, v, K):
            """Generate the x coordinate fron (u, v)."""

            return K * (np.cos(u) * np.cos(2 * v) + np.sqrt(2) * np.sin(u) * np.cos(v))

        def fy(u, v, K):
            """Generate the y coordinate fron (u, v)."""

            return K * (np.cos(u) * np.sin(2 * v) - np.sqrt(2) * np.sin(u) * np.sin(v))

        def fz(u, K):
            """Generate the z coordinate fron (u, v)."""

            return 3 * K * np.cos(u)

        # Build the mesh grid while calculating the (x, y, z) coordinates.
        x = np.vectorize(fx)(u, v, K)
        y = np.vectorize(fy)(u, v, K)
        z = np.broadcast_to(np.vectorize(fz)(u, K), (self.res, self.res))

        return x, y, z
