#coding:utf-8
import unittest
from tools import xml_parser

class ParserTestCase(unittest.TestCase):
    def test_parse_title(self):
        self.assertIn("hongbosb", xml_parser.parse_title("tests/simple_text.html"));

def test_parser():
    unittest.main();
