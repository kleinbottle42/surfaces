"""The catenoid surface."""
import numpy as np
from ..shapes import Shape


class Catenoid(Shape):
    """The Catenoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        res = self.res

        # -180 degrees to 180 degrees in radinas
        u = np.linspace(-np.pi, np.pi, res)

        # Catenoid constant (can be changed)
        c = 0.5

        # Height from -1.0 to 1.0 (can be changed)
        v = np.vstack(np.linspace(-1.0, 1.0, res))

        # Catenoid radius
        r = c * np.cosh(v / c)

        # Convert ploar coordinates to rectangular coordinates
        x = r * np.cos(u)
        y = r * np.sin(u)

        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(v, (res, res))

        return x, y, z
