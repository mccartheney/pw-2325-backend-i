import unittest
import math

class circle :
    def __init__ (self, radio: int) -> None :
        self.radio = radio

    def perimetre (self) -> float :
        return 2 * math.pi * self.radio
    
    def area (self) -> float :
        return math.pi * (self.radio*self.radio)
    
class circleTest (unittest.TestCase) :
    def setUp(self) :
        self.circle = circle(radio = 10)
    
    def test_circle_area (self) -> None :
        result = self.circle.area()
        target = 314.1592653589793238
        self.assertEqual(result, target)

    def test_circle_perimetre (self) -> None:
        result = self.circle.perimetre()
        target = 62.8318530717958648
        self.assertEqual(result, target)

if __name__ == "__main__":
    unittest.main()
