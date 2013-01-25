import tornado.web
import tornado.ioloop
from tornado.template import Template
from tornado.template import Loader

class MainHandler(tornado.web.RequestHandler):
    def get(self):
	loader = Loader("./")
	self.write(loader.load("base.html").generate(**(self.build_values())))

    def build_values(self):
        return {"students" : ["shijie", "hongxia", "hongbo"], "test2":"test2",}

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        loader = Loader("./")
        self.write(loader.load("about.html").generate())


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/about.html", AboutHandler),
    (r"/index.html", MainHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./static/"}),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "./css/"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "./js/"}),
    ]);

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
