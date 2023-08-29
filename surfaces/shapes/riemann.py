"""Riemann."""
import numpy as np
from ..shapes import Shape


class Riemann(Shape):
    """The Riemann shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.linspace(-np.pi, np.pi, self.res)
        v = np.vstack(np.linspace(-2 * np.pi, 2 * np.pi, self.res))
        k = 3 / 10
        w = np.vectorize(complex)(u, v)
        j = complex(0, 1)
        a = 1

        def fx(w):
            """Generate the x coordinate fron (u, v)."""
            return a * np.real((1 - k**2) * w + (8 * (k**2) * w)/(w**2 -1))

        def fy(w):
            return a * np.real(j * ((1 + k**2) * w - (8 * (k**2) * w)/(w**2 -1)))


        def fz(w):
            return a * np.real(k *(w + 2 * np.log((w - 1)/(w + 1))))

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(w)
        y = np.vectorize(fy)(w)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.vectorize(fz)(w)

        return x, y, z
