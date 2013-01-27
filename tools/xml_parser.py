from xml.dom.minidom import parse

TITLE_TAGS = ["h1", "h2", "h3"];

def parse_title(file_path):
    dom = parse(file_path);
    title = ""
    for tag in TITLE_TAGS:
        title = get_title(dom, tag);
        if title is not None:
            return title;

def get_title(dom, tag):
    elements = dom.getElementsByTagName(tag);
    if len(elements) == 0 or len(elements[0].childNodes) == 0:
        return None;
    else:
        try: 
            return elements[0].childNodes[0].data;
        except Error:
            #When the first node is not a text node, then just return empty string.            
            return None;
