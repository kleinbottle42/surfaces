"""Whitney's Umbrella."""
import numpy as np
from ..shapes import Shape


class WhitneysUmbrella(Shape):
    """The Whitney's Umbrella shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        u = np.vstack(np.linspace(-200, 200, self.res))
        v = np.linspace(-200, 200 , self.res)

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return u * v


        def fz(v):
            return v**2

        # Generate the coordinates based on the functions
        x = np.vectorize(fx)(u, v)
        y = np.broadcast_to(u, (self.res, self.res))
        # Ensure z is fits the size of the (x, y) dataa
        z = np.broadcast_to(np.vectorize(fz)(v), (self.res, self.res))

        return x, y, z
