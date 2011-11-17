#! /usr/bin/python

import cgitb; cgitb.enable()
import sys
import web
from web.contrib.template import render_jinja
from ScriptingBridge import SBApplication

def cgidebugerror():
    """                                                                         
    """
    _wrappedstdout = sys.stdout

    sys.stdout = web._oldstdout
    cgitb.handler()

    sys.stdout = _wrappedstdout

web.internalerror = cgidebugerror

urls = (
    r'/.*', 'nowplaying')

app = web.application(urls, globals())

# render = web.template.render('templates/')

render = render_jinja(
        'templates',            # Set template directory.
        encoding = 'utf-8',     # Encoding.
    )

class nowplaying:
    def GET(self):
        
        iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
        track = iTunes.currentTrack()
        
        web.header('Content-Type','text/html; charset=utf-8') 
        return render.nowplaying(track=track, iTunes=iTunes, len=len)

if __name__ == "__main__":
    app.run()
