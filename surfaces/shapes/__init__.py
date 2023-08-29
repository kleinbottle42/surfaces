"""The generic shape class."""
import numpy as np


def calc_plotly_contour(coordinates, res):
    """Calculate the plotly contour."""

    mn = np.amin(coordinates)
    mx = np.amax(coordinates)
    return dict(color='purple', show=True, start=mn, end=mx, size=abs(mx - mn) / res)


class Shape:
    """The shape object."""

    def __init__(self, resolution=50, plotter='plotly', edges=True):
        """Initialize."""

        self.res = resolution
        self.plotter = plotter
        self.edges = edges

    def calculate(self):
        """Calculate the the shape coordinates."""

    def plot(self):
        """Plot the shape."""

        x, y, z = self.calculate()

        if self.plotter == 'plotly':
            import plotly.graph_objects as go
            import plotly.colors as colors

            fig = go.Figure(
                data=[
                    go.Surface(
                        x=x, y=y, z=z,
                        colorscale=colors.get_colorscale('plotly3'),
                        contours=dict(
                            x=calc_plotly_contour(x, self.res),
                            y=calc_plotly_contour(y, self.res),
                            z=calc_plotly_contour(z, self.res)
                        ) if self.edges else dict()
                    )
                ]
            )
            fig.show()

        elif self.plotter == 'matplotlib':
            import matplotlib.pyplot as plt

            # Setup figure
            figure = plt.figure()
            ax = plt.axes(projection='3d')
            figure.add_axes(ax)

            # Plot surface
            ax.plot_surface(
                x, y, z,
                cmap='cool',
                shade=True,
                edgecolor='purple' if self.edges else '#00000000',
                antialiased=True,
                alpha=0.8
            )
            plt.show()
