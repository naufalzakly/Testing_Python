import unittest
from  suhu_testingLibrary import Suhuu

class TestSuhu(unittest.TestCase):

    def test_Faranheit(self):
        result_Faranheit = Suhuu.CelciusConvertFaranheit(30)
        self.assertEqual(result_Faranheit,86 )

    def test_Reamur(self):
        result_Reamur = Suhuu.CelciusConvertReamur(30)
        self.assertEqual(result_Reamur, 24)
    
    def test_Kelvin(self):
        result_Kelvin = Suhuu.CelciusConvertKelvin(30)
        self.assertEqual(result_Kelvin, 303.15)

    unittest.main()
