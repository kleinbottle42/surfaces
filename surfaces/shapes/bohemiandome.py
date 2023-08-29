import numpy as np
from ..shapes import Shape


class BohemianDome(Shape):
    """The Catenoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        res = self.res

        u = np.linspace(-np.pi, np.pi, res)
        v = np.vstack(np.linspace(-np.pi, np.pi, res))
        a = 1
        b = 2

        def fx(u):
            """Generate the x coordinate fron (u, v)."""

            return a * np.cos(u)

        def fy(v):
            """Generate the y coordinate fron (u, v)."""

            return b * np.cos(v)

        def fz(u, v):
            """Generate the z coordinate fron (u, v)."""

            return a * np.sin(u) + b * np.sin(v)

        # Build the mesh grid while calculating the (x, y, z) coordinates.
        x = np.broadcast_to(np.vectorize(fx)(u), (res, res))
        y = np.broadcast_to(np.vectorize(fy)(v), (res, res))
        z = np.vectorize(fz)(u, v)

        return x, y, z
