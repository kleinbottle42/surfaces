import numpy as np
from ..shapes import Shape


class Berlingot(Shape):
    """The Catenoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        res = self.res

        u = np.linspace(-2*np.pi, 2*np.pi, res)
        v = np.vstack(np.linspace(-2*np.pi, 2*np.pi, res))
        a = 1
        k = 10

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return k * a * (1 + u) * np.cos(v)

        def fy(u, v):
            """Generate the y coordinate fron (u, v)."""

            return k * a * (1 - u) * np.sin(v)

        def fz(u):
            """Generate the z coordinate fron (u, v)."""

            return a * u

        # Build the mesh grid while calculating the (x, y, z) coordinates.
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        z = np.broadcast_to(np.vectorize(fz)(u), (res, res))

        return x, y, z