# -*- coding: utf-8 -*-
import xbmc
import urllib2

class Monitor(xbmc.Monitor):
    def __init__(self):
        xbmc.Monitor.__init__(self)

    def onNotification(self, sender, method, data):
        global susppend_auto_change
        global set_for_susspend
        api_base_url = 'http://localhost:29445/API'

        if 'Player.OnStop' in method:
            try:
                url = '%s?command=OFF' % (api_base_url)
                response = urllib2.urlopen(url)
                response.read()
                pass
            except:
                pass
        if 'Player.OnPlay' in method:
            try:
                url = '%s?command=ON' % (api_base_url)
                response = urllib2.urlopen(url)
                response.read()
                pass
            except:
                pass

# Disable on first start in case Kodi was closed improperly and left it on
try:
    url = '%s?command=OFF' % (api_base_url)
    response = urllib2.urlopen(url)
    response.read()
    pass
except:
    pass

monitor = Monitor()

while (not xbmc.abortRequested):
    xbmc.sleep(100)
