import sys
import sqlite3
from db import *;

def update_db():
    print "update_db";

def delete_db():
    conn = get_connection();
    c = conn.cursor();
    c.execute("DROP TABLE IF EXISTS blog");
    conn.commit();
    c.close();

def create_db():
    conn = get_connection();
    c = conn.cursor();
    c.execute("DROP TABLE IF EXISTS blog");
    c.execute('''CREATE TABLE 
                blog(_id INTEGER PRIMARY KEY AUTOINCREMENT, title text, url text)''');
    conn.commit();
    c.close();

methods_dict = dict(update=update_db, create=create_db);

def is_argument_valid():
    return len(sys.argv) == 2 and sys.argv[1] in methods_dict.keys();

if __name__ == "__main__":
    if not is_argument_valid():
        print "Usage: ./db_tools.py <update|create>";
    else:
        methods_dict[sys.argv[1]]()
