import numpy as np
from ..shapes import Shape


class Figure8Klein(Shape):
    """The Catenoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        res = self.res

        theta = np.linspace(0, 2 * np.pi, res)
        v = np.vstack(np.linspace(0, 2 * np.pi, res))
        r = 3


        def fx(t, v):
            """Generate the x coordinate fron (u, v)."""

            return (r + np.cos(t/2) * np.sin(v ) - np.sin(t/2) * np.sin(2 * v)) * np.cos(t)

        def fy(t, v):
            """Generate the y coordinate fron (u, v)."""

            return (r + np.cos(t/2) * np.sin(v) - np.sin(t/2) * np.sin(2 * v)) * np.sin(t)

        def fz(t, v):
            return np.sin(t/2) * np.sin(v) - np.cos(t/2) * np.sin(2 * v)


        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(theta, v)
        y = np.vectorize(fy)(theta, v)
        z = np.broadcast_to(np.vectorize(fz)(theta, v), (res, res))

        

        return x, y, z