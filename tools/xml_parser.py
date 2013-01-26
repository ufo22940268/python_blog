from xml.dom.minidom import parse, parseString

def parse_title(file_path):
    dom = parse(file_path);
    nodeList = dom.getElementsByTagName("h2")
    if len(nodeList) == 0:
        return "";
    else:
        print nodeList[0].childNodes[0].data
        return nodeList[0]
