import numpy as np
from ..shapes import Shape


class CartansUmbella(Shape):
    """The Catenoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        res = self.res

        u = np.vstack(np.linspace(0, 1, res))
        v = np.linspace(0, 2 * np.pi , res)

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return u * np.cos(v) 


        def fy(u, v):
            return u * np.sin(v)

        def fz(u, v):
            return u * np.cos(v)**3 


        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y = np.vectorize(fy)(u, v)
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(u, v), (res, res))

        return x, y, z