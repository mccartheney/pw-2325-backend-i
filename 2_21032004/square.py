import unittest

class square :
    def __init__ (self, width, height) :
        self.width = width
        self.height = height

    def area (self) :
        return self.height * self.width
    
    def perimetre (self) :
        return (2 * self.height) + (2 * self.width)
    
class TestPerimetreAndArea (unittest.TestCase) :
    
    def test_case_1(self) :
        height = 2
        width = 2
        squareTest = square(width, height)

        area_value = squareTest.area()
        perimetre_value = squareTest.perimetre()

        result = [area_value, perimetre_value]

        solution_target = [4, 8]

        self.assertEqual(result, solution_target)

    def test_case_2(self) :
            height = 4
            width = 4
            squareTest = square(width, height)

            area_value = squareTest.area()
            perimetre_value = squareTest.perimetre()

            result = [area_value, perimetre_value]

            solution_target = [16, 16]

            self.assertEqual(result, solution_target)


if __name__ == "__main__":
    unittest.main()
