"""The catenoid surface."""
import numpy as np
from ..shapes import Shape

# Catenoid constant (can be changed)
a = 1


def fx(u, v):
    """Generate the x coordinate fron (u, v)."""

    return a * np.cos(u)**3 * np.cos(v)**3


def fy(u, v):
    """Generate the y coordinate fron (u, v)."""

    return a * np.sin(u)**3 * np.cos(v)**3


def fz(v):
    """Generate the z coordinate fron (u, v)."""

    return a * np.sin(v)**3


class AstroidalSurface(Shape):
    """The Catenoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        res = self.res

        # -180 degrees to 180 degrees in radinas
        u = np.linspace(-2*np.pi, 2*np.pi, res)

        # Height from -1.0 to 1.0 (can be changed)
        v = np.vstack(np.linspace(-2*np.pi, 2*np.pi, res))

        # Build the mesh grid while calculating the (x, y, z) coordinates.
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        z = np.broadcast_to(np.vectorize(fz)(v), (res, res))
        return x, y, z
