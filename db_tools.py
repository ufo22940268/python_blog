import sys
import sqlite3
import tools.xml_parser
import os
from tools.db import *;

def update_db(folder):
    clear_blog_table();

    conn = get_connection();
    c = conn.cursor();
    for f in os.listdir("./" + folder):
        if not is_html(f): continue;
        full_file = folder + "/" + f;
        c.execute("INSERT INTO blog(title, url) values(?, ?)",
                (tools.xml_parser.parse_title(full_file).decode("utf-8"), full_file));
    conn.commit();
    c.close();

def is_html(file_path):
    return file_path.endswith(".html");

def update_db_for_tests():
    update_db("tests");

def update_db_for_blog():
    update_db("blog");

def clear_blog_table():
    conn = get_connection();
    c = conn.cursor();
    c.execute("DELETE FROM blog");
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

def print_blog_table():
    conn = get_connection();
    c = conn.cursor();
    c.execute("SELECT * FROM blog");
    conn.commit();
    for r in c.fetchall():
        print r
    c.close();

methods_dict = dict(update=update_db_for_blog, create=create_db, print_blog=print_blog_table);

def is_argument_valid():
    return len(sys.argv) == 2 and sys.argv[1] in methods_dict.keys();

if __name__ == "__main__":
    if not is_argument_valid():
        print "Usage: ./db_tools.py <update|create|print_blog>";
    else:
        methods_dict[sys.argv[1]]()
