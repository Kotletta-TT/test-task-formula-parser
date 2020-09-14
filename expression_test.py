import unittest
from app import get_answer


class MyTestCase(unittest.TestCase):

    def test_simple_expression(self):
        self.assert_expression(input='expr=2+2', right_answer=4)

    def test_combine_expression(self):
        self.assert_expression(input='expr=(2+2)+4**2/(89+(77-3))', right_answer=4.098159509202454)

    def test_floor_expression(self):
        self.assert_expression(input='expr=math.floor(3.2456)', right_answer=3)

    def assert_expression(self, input, right_answer):
        output = get_answer(input)
        self.assertEqual(output, right_answer)


if __name__ == '__main__':
    unittest.main()
