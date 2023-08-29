"""Heliocoid."""
import numpy as np
from ..shapes import Shape


class Heliocoid(Shape):
    """The Heliocoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        theta = np.vstack(np.linspace(-np.pi, np.pi, self.res))
        rho = np.linspace(-1.0, 1.0, self.res)
        alpha = 1

        def fx(r, t):
            """Generate the x coordinate fron (u, v)."""

            return r * np.cos(alpha * t)

        def fy(r, t):
            """Generate the y coordinate fron (u, v)."""

            return r * np.sin(alpha * t)

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(rho, theta)
        y = np.vectorize(fy)(rho, theta)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(theta, (self.res, self.res))

        return x, y, z
