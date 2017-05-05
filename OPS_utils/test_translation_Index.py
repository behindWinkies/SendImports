import unittest
from Translation_Index import Translation_Index
import os
import sys
from whoosh import searching
from whoosh.qparser import QueryParser

class TestTranslation_Index(unittest.TestCase):

    # origin_path = 'C:/E-Commerce/Test1'
    origin_path = r'\\brnpim7pro01\folders\ImportArchive\Translations\TPlus'
    index_directory = "indexdir"
    index_name = "trans_index"
    index = Translation_Index(origin_path,index_directory, index_name)

    # def test_create_index(self):
    #
    #     path = self.origin_path
    #     direc = self.index_directory
    #     test_index = self.index
    #     test_index.create_index()
    #     os.chdir(path)
    #
    #     if os.path.isdir(direc):
    #         result = True
    #     else:
    #         self.fail()
    #
    #     return result

    def test_def_index_files(self):
        # #start = sys.getsizeof(test_index)
        # test_index = self.index.index_files()
        # end = sys.getsizeof(test_index)
        # print (test_index)
        # self.fail()
        #
        result = self.index.index_files()
        if not result:
            self.fail()
        else:
            return True

    # def test_get_translations(self):
    #
    #     file1 = 'mx_integration_Brand3 - 791329 - da.xml'
    #     file2 = 'mx_integration_Brand3 - 791330 - nl.xml'
    #
    #     result_list = self.index.get_translations(13140011)
    #     bool1 = False
    #     bool2 = False
    #
    #     # Test
    #     for list in result_list:
    #
    #         if file1 in list:
    #             bool1 = True
    #         if file2 in list:
    #             bool2 = True
    #
    #     # print (result_list)
    #
    #     if bool1 and bool2:
    #         return True
    #     else:
    #         self.fail()
    #
    # def test_get_most_recent (self):
    #
    #     file1 = 'mx_integration_Brand3 - 791329 - da.xml'
    #     file2 = 'mx_integration_Brand8 - 788883 - nl.xml'
    #     result_list = self.index.get_most_recent(13140011)
    #
    #     if file1 in result_list and file2 in result_list:
    #         return True
    #     else:
    #         self.fail()

if __name__ == '__main__':
    unittest.main()
