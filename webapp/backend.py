from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import asyncio

import json

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
 
import text2story as t2s

class Handler(RequestHandler):
    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))

        narrative = t2s.Narrative(lang=data['lang'],
                                  text=data['text'],
                                  publication_time=data['publication_time'])

        narrative.extract_actors(*data['actor_extraction_tools'])
        narrative.extract_times(*data['time_extraction_tools'])
        narrative.extract_events(*data['event_extraction_tools'])
        # narrative.extract_objectal_links(*data['objectal_link_extraction_tools'])
        narrative.extract_semantic_role_links(*data['semantic_role_link_extraction_tools'])

        self.write(narrative.ISO_annotation())
        
class TestHandler(RequestHandler):
    def get(self):
        self.write("Hello World!")

if __name__ == '__main__':
    t2s.start()

    app = Application([
        (r"/", Handler),
        (r"/test", TestHandler)
    ])
    http_server = HTTPServer(app)
    
    # Create new event loop for the new thread
    asyncio.set_event_loop(asyncio.new_event_loop())
    
    http_server.listen(8888)

    print('Finished configuring')

    IOLoop.instance().start()
