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
        
        if iTunes.isRunning() and iTunes.playerState() == 1800426320:
            track = iTunes.currentTrack()

            # print [i for i in dir(iTunes) if "_" not in i]

            # if iTunes.currentPlaylist().name() == "Music" or len(iTunes.currentPlaylist().tracks()) > 200:
            #     print "<h2>Current Track: %s - %s</h2>" % (track.artist(), track.name())
            # else:
            #     print "<ul><strong>Current Playlist: %s</strong>" % iTunes.currentPlaylist().name()
            #     for tr in iTunes.currentPlaylist().tracks():
            #         if tr.name() == track.name() and tr.artist() == track.artist():
            #             print "<li style='color:blue'>%s - %s</li>" % (tr.artist(), tr.name())
            #         else:
            #             print "<li>%s - %s</li>" % (tr.artist(), tr.name())
            # print "</ul>"
        
        web.header('Content-Type','text/html; charset=utf-8') 
        return render.nowplaying()

if __name__ == "__main__":
    app.run()
