"""Mobius Strip."""
import numpy as np
from ..shapes import Shape


class MobiusStrip(Shape):
    """The Mobius Strip shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        # Generate the (u, v) coordinates
        u = np.linspace(0, 2 * np.pi, self.res)
        v = np.linspace(-1, 1, self.res)

        #Cross section (Uncomment to get cross section)
        # u = np.linspace(0, np.pi, 50)
        # v = np.linspace(0, 2 * np.pi, 50)

        def fx(u, v):
            """Generate the x coordinate fron (u, v)."""

            return (1 + v/2 * np.cos(u/2)) * np.cos(u) 
            

        def fy(u, v):
            """Generate the y coordinate fron (u, v)."""

            return (1 + v/2 * np.cos(u/2)) * np.sin(u) 

        def fz(u, v):
            """Generate the z coordinate fron (u, v)."""

            return v/2 * np.sin(u/2)

        # Build the mesh grid while calculating the (x, y, z) coordinates.
        z = []
        x = []
        y = []
        for c1 in u:
            x.append([])
            y.append([])
            z.append([])
            for c2 in v:
                # Calculate the rectangular coordinates
                x[-1].append(fx(c1, c2))
                y[-1].append(fy(c1, c2))
                # Save the current z for each (x, y) point
                z[-1].append(fz(c1, c2))

        return x, y, z
