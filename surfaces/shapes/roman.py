"""Roman."""
import numpy as np
from ..shapes import Shape


class Roman(Shape):
    """The Roman shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        a = 0
        u = np.vstack(np.linspace(-np.pi/2, np.pi/2, self.res))
        v = np.linspace(0, np.pi, self.res)

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return (np.sqrt(2) * np.cos(2 * u) * np.cos(v)**2
                + np.cos(u) * np.sin(2 * v))/(2 - a * np.sqrt(2) * 
                np.sin(3 * u) * np.sin(2 * v))

        def fy(u, v):
            return (np.sqrt(2) * np.sin(2 * u) * np.cos(v)**2
                - np.sin(v) * np.sin(2 * v))/(2 - a * np.sqrt(2) * 
                np.sin(3 * u) * np.sin(2 * v))

        def fz(u, v):
            return (3 * np.cos(v)**2)/(2 - a * np.sqrt(2) * 
                np.sin(3 * u) * np.sin(2 * v))

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(u, v), (self.res, self.res))

        return x, y, z
