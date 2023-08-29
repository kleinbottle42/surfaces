"""The main entry point and command line interface for the shape library."""
import argparse
import sys
from .shapes.catenoid import Catenoid
from .shapes.astroidalsurface import AstroidalSurface
from .shapes.berlingot import Berlingot
from .shapes.bohemiandome import BohemianDome
from .shapes.bryantkusner import BryantKusner
from .shapes.cartansumbrella import CartansUmbella
from .shapes.catalinssurface import CatalinsSurface
from .shapes.crosscappeddisk import CrosscappedDisk
from .shapes.dinissurface import DinisSurface
from .shapes.ennepersurface import EnneperSurface
from .shapes.figure8klein import Figure8Klein
from .shapes.gabrielstrumpet import GabrielsTrumpet
from .shapes.torus import Torus
from .shapes.sphere import Sphere
from .shapes.apery import Apery
from .shapes.kleinbottle import KleinBottle
from .shapes.heliocoid import Heliocoid
from .shapes.whitneysumbrella import WhitneysUmbrella
from .shapes.horntorus import HornTorus
from .shapes.mobiusstrip import MobiusStrip
from .shapes.riemann import Riemann
from .shapes.lame import Lame
from .shapes.pluckersconoid import PluckersConoid
from .shapes.tanneryspear import TannerySpear
from .shapes.pressuretower import PressureTower
from .shapes.morinapery import MorinApery
from .shapes.roman import Roman
from .shapes.selfintersectingdisk import SelfIntersectingDisk
from .shapes.sinussurface import SinusSurface
from .shapes.surfacedegal import SurfaceDegal
from .shapes.wallissconicaledge import WallissConicalEdge

shapes = {
	'catenoid': Catenoid,
	'astroidalsurface': AstroidalSurface,
	'berlingot': Berlingot,
	'bohemiandome': BohemianDome,
	'bryantkusner': BryantKusner,
	'cartansumbrella': CartansUmbella,
	'catalinssurface': CatalinsSurface,
	'crosscappeddisk': CrosscappedDisk,
	'dinissurface': DinisSurface,
	'ennepersurface': EnneperSurface,
	'figure8klein': Figure8Klein,
	'gabrielstrumpet': GabrielsTrumpet,
	'torus': Torus,
	'sphere': Sphere,
	'apery': Apery,  # Not working
	'kleinbottle': KleinBottle,
	'heliocoid': Heliocoid,
	'whitneysumbrella': WhitneysUmbrella,
	'horntorus': HornTorus,
	'mobiusstrip': MobiusStrip,
	'riemann': Riemann,  # Mostly working
	'lame': Lame, # Not working
	'pluckersconoid': PluckersConoid,
	'tanneryspear': TannerySpear,
	'pressuretower': PressureTower,
	'morinapery': MorinApery,
	'roman': Roman,
	'selfintersectingdisk': SelfIntersectingDisk,
	'sinussurface': SinusSurface,
	'surfacedegal': SurfaceDegal,
	'wallissconicaledge': WallissConicalEdge
}


def main():
	"""The main CLI."""

	parser = argparse.ArgumentParser(prog='plotshape', description='Plot various shapes.')
	parser.add_argument('--shape', '-s', help="The shape name to plot.")
	parser.add_argument('--plotter', '-p', default="plotly", help="The plot library to use.")
	parser.add_argument('--resolution', '-r', type=int, default=50, help="The default resolution to use.")
	parser.add_argument('--no-edges', '-e', action='store_true', help="Turn off edges.")
	args = parser.parse_args()

	shape_class = shapes.get(args.shape)
	if shape_class is None:
		raise ValueError(f'Cannot find {args.shape}')
	shape = shape_class(resolution=args.resolution, plotter=args.plotter, edges=not args.no_edges)
	shape.plot()
	raise SystemExit(0)

if __name__ == '__main__':
	main()