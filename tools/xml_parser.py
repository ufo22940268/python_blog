#coding:utf-8
from xml.dom.minidom import parse
from xml.parsers import expat
from utils.string_utils import *
from utils.xml_utils import *
import codecs

TITLE_TAGS = ["h1", "h2", "h3"];
ABBREV_LINE_COUNT = 5;

#The condition that a tag considered as title is 
#* it's using a title tags such as `h1`, `h2`, `h3`.
#* Its class name is *title*.
def parse_title(file_path):
    dom = parse(file_path);
    title = ""
    for tag in TITLE_TAGS:
        title = get_title(dom, tag);
        if title is not None:
            return to_utf8(title);

def get_title(dom, tag):
    elements = dom.getElementsByTagName(tag);
    if len(elements) == 0 or len(elements[0].childNodes) == 0:
        return None;
    else:
        if elements[0].hasChildNodes():
            node = elements[0].childNodes[0];
            while node.hasChildNodes():
                node = node.childNodes[0];
            if node.nodeType == node.TEXT_NODE:
                return node.data;
            else:
                return None;
        else:
            return None;

def get_line_of_string(file_path, title):
    lines = open(file_path).readlines();
    for l in xrange(len(lines)):
        if lines[l].find(title) != -1:
            return l;
    else:
        return -1

def parse_abbrev(file_path):
    title = parse_title(file_path);
    line = get_line_of_string(file_path, title)

    if line == -1:
        return -1;
    else:
        return "".join(open(file_path).readlines()[line + 1:ABBREV_LINE_COUNT]);
