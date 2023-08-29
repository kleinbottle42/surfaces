import numpy as np
from ..shapes import Shape


class BryantKusner(Shape):
    """The Catenoid shape class."""

    def calculate(self):
        """Calculate the shape coordinates."""

        res = self.res

        j = complex(0, 1)
        u = np.linspace(0, 1, res)
        v = np.vstack(np.linspace(0, 2 * np.pi, res))
        Z = u * np.exp(j * v)



        def fg1(Z):
            """Generate the x coordinate fron (u, v)."""

            return -3/2 * np.imag((Z * (1 - Z**4))/(Z**6 + np.sqrt(5) * Z**3 -1))

        def fg2(Z):
            """Generate the y coordinate fron (u, v)."""

            return -3/2 * np.real((Z * (1 + Z**4))/(Z**6 + np.sqrt(5) * Z**3 -1))

        def fg3(Z):
            """Generate the z coordinate fron (u, v)."""

            return (np.imag((1 + Z**6)/(Z**6 + np.sqrt(5) * Z**3 -1))) - 1/2

        def fg():
            return fg1(Z)**2 + fg2(Z)**2 + fg3(Z)**2


        # Build the mesh grid while calculating the (x, y, z) coordinates.
        g1 = np.vectorize(fg1)(Z)
        g2 = np.vectorize(fg2)(Z)
        g3 = np.vectorize(fg3)(Z)
        g = np.vectorize(fg)()

        x = g1 / g
        y = g2 / g
        z = g3 / g

        return x, y, z