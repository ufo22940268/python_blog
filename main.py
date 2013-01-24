import tornado.web
import tornado.ioloop
from tornado.template import Template
from tornado.template import Loader

class MainHandler(tornado.web.RequestHandler):
    def get(self):
	loader = Loader("./")
	self.write(loader.load("test.html").generate(**(self.buildValues())))

    def buildValues(self):
        #return dict(hongbosb="hongbosb is not sb")
        return {"hongbosb": "hongbosb is not sbaaaaaa"}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./"}),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "./css/"}),
    ]);

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
