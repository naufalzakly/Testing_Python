import unittest
from unittest import result
import suhu_testingLibrary

class TestMSI(unittest.TestCase):
    
    def test_MIT(self):
        result = suhu_testingLibrary.massaIndexTubuh (60,2.0)
        self.assertEqual(result, 15.0)
    
    def test_Faranheit(self):
        result_Faranheit = suhu_testingLibrary.suhuConvertFaranheit(30)
        self.assertEqual(result_Faranheit,86 )

    def test_Reamur(self):
        result_Faranheit = suhu_testingLibrary.suhuConvertReamur(30)
        self.assertEqual(result_Faranheit, 24)
    
    def test_Kelvin(self):
        result_Faranheit = suhu_testingLibrary.suhuConvertKelvin(30)
        self.assertEqual(result_Faranheit, 303.15)
if __name__ == '__main__':
    unittest.main()