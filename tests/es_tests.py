import unittest
from coval.es import *

class CodeValidatorEsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_cif(self):
        self.assertTrue(cif('A58818501'))
        self.assertTrue(cif('B00000000'))
        self.assertTrue(cif('C0000000J'))
        self.assertTrue(cif('D00000000'))
        self.assertTrue(cif('E00000000'))
        self.assertTrue(cif('F00000000'))
        self.assertTrue(cif('G00000000'))
        self.assertTrue(cif('H00000000'))
        self.assertFalse(cif('I00000000'))
        self.assertFalse(cif('I0000000J'))
        self.assertTrue(cif('J00000000'))
        self.assertTrue(cif('K0000000J'))
        self.assertTrue(cif('L0000000J'))
        self.assertTrue(cif('M0000000J'))
        self.assertTrue(cif('N0000000J'))
        self.assertFalse(cif('O00000000'))
        self.assertFalse(cif('O0000000J'))
        self.assertTrue(cif('P0000000J'))
        self.assertTrue(cif('Q0000000J'))
        self.assertTrue(cif('R0000000J'))
        self.assertTrue(cif('S0000000J'))
        self.assertFalse(cif('T00000000'))
        self.assertFalse(cif('T0000000J'))
        self.assertTrue(cif('U00000000'))
        self.assertTrue(cif('V00000000'))
        self.assertTrue(cif('W0000000J'))
        self.assertFalse(cif('X00000000'))
        self.assertFalse(cif('X0000000J'))
        self.assertFalse(cif('Y00000000'))
        self.assertFalse(cif('Y0000000J'))
        self.assertFalse(cif('Z00000000'))
        self.assertFalse(cif('Z0000000J'))
        self.assertFalse(cif('B0000000J'))
        self.assertFalse(cif('BC0000000'))
        self.assertFalse(cif('123456678'))
        self.assertTrue(cif('B-00000000', strict=False))
        self.assertFalse(cif('B-00000000', strict=True))
        self.assertTrue(cif('K-0000000-J', strict=False))
        self.assertFalse(cif('K-0000000-J', strict=True))

    def test_ccc(self):
        self.assertTrue(ccc('2077-0024-00-3102575766',strict=False))
        self.assertFalse(ccc('2034 4505 73 1000034682',strict=False))
        self.assertTrue(ccc('0000 0000 00 0000000000',strict=False))
        self.assertFalse(ccc('0',strict=False))
        self.assertFalse(ccc('1111 1111 11 1111111111',strict=False))
        self.assertTrue(ccc('0001 0001 65 0000000001',strict=False))
        self.assertFalse(ccc('',strict=False))

        self.assertFalse(ccc('2077 0024 00 3102575766',strict=True))
        self.assertFalse(ccc('0000 0000 00 0000000000',strict=True))
        self.assertFalse(ccc('0001 0001 65 0000000001',strict=True))

        self.assertTrue(ccc('20770024003102575766',strict=True))
        self.assertFalse(ccc('20344505731000034682',strict=True))
        self.assertTrue(ccc('00000000000000000000',strict=True))
        self.assertFalse(ccc('0',strict=True))
        self.assertFalse(ccc('11111111111111111111',strict=True))
        self.assertTrue(ccc('00010001650000000001',strict=True))
        self.assertFalse(ccc('',strict=True))

    def test_ssn(self):
        self.assertFalse(ssn('720111361735'))
        self.assertTrue(ssn('281234567840'))
        self.assertTrue(ssn('351234567825'))
        self.assertFalse(ssn('35/12345678/25', strict=True))
        self.assertTrue(ssn('35/12345678/25', strict=False))
        self.assertFalse(ssn('35-12345678-25', strict=True))
        self.assertTrue(ssn('35-12345678-25', strict=False))
        self.assertFalse(ssn('35X1234567825'))
        self.assertFalse(ssn('031322136383'))
        self.assertFalse(ssn('72011a361732'))
        self.assertFalse(ssn('73011a361731'))
        self.assertFalse(ssn('03092a136383'))
        self.assertFalse(ssn('03132a136385'))
        self.assertFalse(ssn('201113617312'))
        self.assertFalse(ssn('301113617334'))
        self.assertFalse(ssn('309221363823'))
        self.assertFalse(ssn('313221363822'))

    def test_postcode(self):
        self.assertTrue(postcode('28080'))
        self.assertTrue(postcode('35500'))
        self.assertFalse(postcode('59000'))
        self.assertTrue(postcode('12012'))
        self.assertTrue(postcode('25120'))
        self.assertFalse(postcode('10'))
        self.assertFalse(postcode('X123'))

if __name__ == '__main__':
    unittest.main()
