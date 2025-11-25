import unittest
from square import area as S 
from square import perimeter as P

class SquareTestCase(unittest.TestCase):
   def test_zero_side(self):
       res = S(0)
       self.assertEqual(res, 0)
       res = P(0)
       self.assertEqual(res, 0)

   def test_negativ_valueS(self):
       with self.assertRaises(ValueError):
           S(-5)

   def test_negativ_valueP(self):
       with self.assertRaises(ValueError):
           P(-5)

   def test_type_valueS(self):
       with self.assertRaises(TypeError):
           S("5")

   def test_type_valueP(self):
       with self.assertRaises(TypeError):
           P("5")

   def test_standart_area(self):
       res = S(5)
       self.assertEqual(res, 25)

   def test_standart_perimetr(self):
       res = P(5)
       self.assertEqual(res, 20)