import unittest
import os
from Translation_XML import Translation_XML

class TestTranslation_XML(unittest.TestCase):
    pass

    test_file = r'C:/E-Commerce/Test1/mx_integration_Brand1 - 417440 - es.xml'
    test_trans_xml = Translation_XML(test_file)

    def test_edisn_list(self):

        list = self.test_trans_xml.edisn_list()
        result = False
        if 12090375 in list and 12090373 in list:
            result = True
        else:
            self.fail()
        return result

    def test_get_country(self):

        string1 = 'mx_integration_Brand1 - 417436 - fi'
        string2 = 'mx_integration_Brand1 - 417436 - fi.xml'
        bool1 = self.test_trans_xml.get_country(string1) == 'fi'
        bool2 = self.test_trans_xml.get_country(string2) == 'fi'

        if bool1 and bool2:
            return True
        else:
            self.fail()


if __name__ == '__main__':
    unittest.main()