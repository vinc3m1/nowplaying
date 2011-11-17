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
    def POST(self):
        
        iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
        track = iTunes.currentTrack()
        
        i = web.input(submit = None)
        
        if i.submit == "play":
            iTunes.playpause()
        elif i.submit == "next":
            iTunes.nextTrack()
        elif i.submit == "prev":
            iTunes.previousTrack()
        
        web.header('Content-Type','text/html; charset=utf-8') 
        return render.nowplaying(track=track, iTunes=iTunes, len=len)
        

if __name__ == "__main__":
    app.run()
