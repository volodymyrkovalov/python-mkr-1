import unittest

from quadriliterals.isoscelestrapezium import IsoscelesTrapezium
from quadriliterals.parallelogram import Parallelogram
from quadriliterals.rectangle import Rectangle
from quadriliterals.righttrapezium import RightTrapezium
from quadriliterals.rombus import Rhombus
from quadriliterals.square import Square
from quadriliterals.trapezium import Trapezium


class TestGeometryShapes(unittest.TestCase):

    def test_rectangle_properties(self):
        rectangle = Rectangle([(0, 0), (4, 0), (4, 3), (0, 3)])
        self.assertEqual(rectangle.get_area(), 12.0)
        self.assertEqual(rectangle.get_perimeter(), 14.0)
        self.assertEqual(rectangle.get_diagonals(), (5.0,))
        self.assertEqual(rectangle.get_angles(), (90, 90, 90, 90))

    def test_square_properties(self):
        square = Square([(0, 0), (2, 0), (2, 2), (0, 2)])
        self.assertEqual(square.get_area(), 4.0)
        self.assertEqual(square.get_perimeter(), 8.0)
        self.assertEqual(square.get_diagonals(), (2.8284271247461903,))
        self.assertEqual(square.get_angles(), (90, 90, 90, 90))

    def test_parallelogram_properties(self):
        parallelogram = Parallelogram([(0, 0), (3, 0), (4, 2), (1, 2)])
        self.assertEqual(parallelogram.get_area(), 6.708203932499369)
        self.assertEqual(parallelogram.get_perimeter(), 10.47213595499958)
        self.assertEqual(parallelogram.get_diagonals(), (4.55062676260088, 2.700332584608909))
        self.assertEqual(parallelogram.get_angles(), (120, 60, 120, 60))

    def test_rhombus_properties(self):
        rhombus = Rhombus([(0, 0), (2, 2), (4, 0), (2, -2)])
        self.assertEqual(rhombus.get_area(), 6.928203230275509)
        self.assertEqual(rhombus.get_perimeter(), 11.313708498984761)
        self.assertEqual(rhombus.get_diagonals(), (4.898979485566356, 2.8284271247461903))
        self.assertEqual(rhombus.get_angles(), (120, 60, 120, 60))

    def test_trapezium_properties(self):
        trapezium = Trapezium([(0, 0), (4, 0), (3, 2), (1, 2)])
        self.assertEqual(trapezium.get_area(), 6.0)
        self.assertEqual(trapezium.get_perimeter(), 10.47213595499958)
        self.assertEqual(trapezium.get_diagonals(), (3.605551275463989, 3.605551275463989))
        self.assertEqual(trapezium.get_angles(), (63.43494882292201, 63.43494882292201, 116.56505117707799, 116.56505117707799))

    def test_right_trapezium_properties(self):
        right_trapezium = RightTrapezium([(0, 0), (4, 0), (4, 3), (1, 3)])
        self.assertEqual(right_trapezium.get_area(), 10.5)
        self.assertEqual(right_trapezium.get_perimeter(), 13.16227766016838)
        self.assertEqual(right_trapezium.get_diagonals(), (5.0, 4.242640687119285))
        self.assertEqual(right_trapezium.get_angles(), (90, 90, 90.0, 108.43494882292201))

    def test_isosceles_trapezium_properties(self):
        isosceles_trapezium = IsoscelesTrapezium([(0, 0), (5, 0), (4, 3), (1, 3)])
        self.assertEqual(isosceles_trapezium.get_area(), 12.0)
        self.assertEqual(isosceles_trapezium.get_perimeter(), 14.32455532033676)
        self.assertEqual(isosceles_trapezium.get_diagonals(), (5.0, 5.0))
        self.assertEqual(isosceles_trapezium.get_angles(), (71.56505117707799, 71.56505117707799, 108.43494882292201, 108.43494882292201))


if __name__ == '__main__':
    unittest.main()