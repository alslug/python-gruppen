import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "<html><head><title>Hello World!</title></head><body>Hello World!<body></html>"

cherrypy.quickstart(HelloWorld())