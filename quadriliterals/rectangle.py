
import math

from quadriliterals.quadriliteral import Quadrilateral


class Rectangle(Quadrilateral):

    def _calculate_area(self):
        return self.sides[0] * self.sides[1]

    def _calculate_diagonals(self):
        return (math.sqrt(self.sides[0]**2 + self.sides[1]**2),)

    def _calculate_angles(self):
        return (90, 90, 90, 90)