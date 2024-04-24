from quadriliterals.parallelogram import Parallelogram


class Rhombus(Parallelogram):
    def _calculate_area(self):
        # Using diagonals to calculate area of Rhombus: (diagonal1 * diagonal2) / 2
        d1, d2 = self._calculate_diagonals()
        return (d1 * d2) / 2