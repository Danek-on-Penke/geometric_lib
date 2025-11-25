import unittest
from rectangle import area as S 
from rectangle import perimeter as P

class RectangleTestCase(unittest.TestCase):
   def test_zero_side(self):
       res = S(0, 10)
       self.assertEqual(res, 0)
       res = P(0, 0)
       self.assertEqual(res, 0)

   def test_negativ_valueS(self):
       with self.assertRaises(ValueError):
           S(-1, 2)
       with self.assertRaises(ValueError):
           S(1, -2)

   def test_negativ_valueP(self):
       with self.assertRaises(ValueError):
           P(-1, 2)
       with self.assertRaises(ValueError):
           P(1, -2)

   def test_type_valueS(self):
       with self.assertRaises(TypeError):
           S("1", 2)
       with self.assertRaises(TypeError):
           S(1, "2") 

   def test_type_valueP(self):
       with self.assertRaises(TypeError):
           P("1", 2)
       with self.assertRaises(TypeError):
           P(1, "2")  

   def test_standart_area(self):
       res = S(5, 8)
       self.assertEqual(res, 40)

   def test_standart_perimetr(self):
       res = P(5, 8)
       self.assertEqual(res, 26)