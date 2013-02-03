import tornado.web
import tornado.ioloop
from tornado.template import Template
from tornado.template import Loader
from tools.db import *
import sqlite3

class MainHandler(tornado.web.RequestHandler):
    def get(self):
	loader = Loader("./");
	self.write(loader.load("base.html").generate());

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        loader = Loader("./");
        self.write(loader.load("about.html").generate());

class ContentHandler(tornado.web.RequestHandler):

    class Entity:
        pass

    def get(self):
        loader = Loader("./");
        self.write(loader.load("content.html").generate(**(self.build_values())));

    def build_values(self):
        conn = get_connection();
        c = conn.cursor();
        c.execute("SELECT title, url FROM blog");
        rows = c.fetchall();
        entities = [];
        for row in rows:
            entity = ContentHandler.Entity();
            entity.content = row[0];
            entity.url = row[1];
            entities.append(entity);
        return {"entities" : entities};

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/about.html", AboutHandler),
    (r"/index.html", MainHandler),
    (r"/content.html", ContentHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./static/"}),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "./css/"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "./js/"}),
    ]);

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
