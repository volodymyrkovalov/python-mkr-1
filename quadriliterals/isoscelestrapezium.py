from quadriliterals.trapezium import Trapezium


class IsoscelesTrapezium(Trapezium):
    def __init__(self, vertices):
        super().__init__(vertices)
        # Angles for isosceles trapezium where non-parallel sides are equal
        self.angles = (self.angles[0], self.angles[0], self.angles[2], self.angles[2])  # Assuming equal angles at opposite vertices