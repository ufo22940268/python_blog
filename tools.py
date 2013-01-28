import sys

def update():
    print "update db and content html.";

methods_dict = dict(update=update);

def is_argument_valid():
    return len(sys.argv) == 2 and sys.argv[1] in methods_dict.keys();

if __name__ == "__main__":
    if not is_argument_valid():
        print '''Usage python tools.py <update>''';
    else:
        methods_dict[sys.argv[1]]();
