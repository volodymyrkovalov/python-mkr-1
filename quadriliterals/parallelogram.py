import math

from quadriliterals.quadriliteral import Quadrilateral


class Parallelogram(Quadrilateral):
    def _calculate_area(self):
        height = math.sin(math.radians(90)) * self.sides[1]  # Assuming one angle is 90 degrees for simplicity
        return self.sides[0] * height

    def _calculate_diagonals(self):
        return (math.sqrt(self.sides[0]**2 + self.sides[1]**2 - 2*self.sides[0]*self.sides[1]*math.cos(math.radians(120))),
                math.sqrt(self.sides[0]**2 + self.sides[1]**2 - 2*self.sides[0]*self.sides[1]*math.cos(math.radians(60))))

    def _calculate_angles(self):
        return (120, 60, 120, 60)