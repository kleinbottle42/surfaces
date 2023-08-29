"""Klein Bottle."""
import numpy as np
from ..shapes import Shape


class KleinBottle(Shape):
    """The Klein Bottle shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        # Generate the (u, v) coordinates
        min_u = 0
        max_u = np.pi
        u = np.linspace(min_u, max_u, self.res)
        v = np.vstack(np.linspace(min_u * 2, max_u * 2, self.res))

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return -(2 / 15) * np.cos(u) * (
                3 * np.cos(v) -
                30 * np.sin(u) +
                90 * (np.cos(u) ** 4) * np.sin(u) -
                60 * (np.cos(u) ** 6) * np.sin(u) +
                5 * np.cos(u) * np.cos(v) * np.sin(u)
            )

        def fy(u, v):
            """Generate the y coordinate fron (u, v)."""

            return -(1 / 15) * np.sin(u) * (
                3 * np.cos(v) -
                3 * (np.cos(u) ** 2) * np.cos(v) -
                48 * (np.cos(u) ** 4) * np.cos(v) +
                48 * (np.cos(u) ** 6) * np.cos(v) -
                60 * np.sin(u) + 5 * np.cos(u) * np.cos(v) * np.sin(u) -
                5 * (np.cos(u) ** 3) * np.cos(v) * np.sin(u) -
                80 * (np.cos(u) ** 5)* np.cos(v) * np.sin(u) +
                80 * (np.cos(u) ** 7) * np.cos(v) * np.sin(u)
            )

        def fz(u, v):
            """Generate the z coordinate fron (u, v)."""

            return (2 / 15) * (3 + 5 * np.cos(u) * np.sin(u)) * np.sin(v)

        # Build the mesh grid while calculating the (x, y, z) coordinates.
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        z = np.vectorize(fz)(u, v)

        return x, y, z
