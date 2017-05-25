import cherrypy
import json

class HelloWorld(object):
    @cherrypy.tools.accept(media='application/json')
    @cherrypy.expose
    def index(self):
        headers = cherrypy.request.headers.output()
        cherrypy.response.headers['Content-Type'] = 'application/json'
        print headers

        return json.dumps(headers)
cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.quickstart(HelloWorld())
