#coding:utf-8
import unittest
from tools import xml_parser

class ParserTestCase(unittest.TestCase):
    def test_parse_title1(self):
        self.assertEqual("hongbosb", xml_parser.parse_title("tests/simple_text.html"));

    def test_parse_title2(self):
        self.assertEqual("喵的，该写一下博客了", xml_parser.parse_title("blog/1.html"));
        self.assertEqual("边运行junit，边调试，蛋疼", xml_parser.parse_title("blog/2.html"));
        self.assertEqual("android文档查询小工具", xml_parser.parse_title("blog/3.html"));

    def test_parse_abbrev(self):
        print xml_parser.parse_abbrev("blog/1.html");
        self.assertIn("首先学习了", xml_parser.parse_abbrev("blog/1.html"));

def test_parser():
    unittest.main();
