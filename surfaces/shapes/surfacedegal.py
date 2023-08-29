"""Surface D'égal."""

import numpy as np
from ..shapes import Shape


class SurfaceDegal(Shape):
    """The Surface Degal shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        # Generate the (u, v) coordinates
        u = np.linspace(-np.pi / 2, np.pi / 2, self.res)
        v = np.vstack(np.linspace(0, np.pi, self.res))
        a = 10

        def _sqrt(value):
            return np.sign(value) * np.sqrt(np.abs(value))

        sqrt = np.vectorize(_sqrt)

        r = a * sqrt(np.sin(u))

        def fx(r, u, v):
            """Generate the x coordinate fron (u, v)."""

            return r * np.cos(u) * np.cos(v)

        def fy(r, u, v):
            """Generate the y coordinate fron (u, v)."""

            return r * np.cos(u) * np.sin(v)

        def fz(r, u):
            """Generate the z coordinate fron (u, v)."""

            return r * np.sin(u)

        # Build the mesh grid while calculating the (x, y, z) coordinates.
        x = np.vectorize(fx)(r, u, v)
        y = np.vectorize(fy)(r, u, v)
        z = np.broadcast_to(np.vectorize(fz)(r, u), (self.res, self.res))

        return x, y, z
