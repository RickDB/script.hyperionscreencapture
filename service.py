# -*- coding: utf-8 -*-
import xbmc
import urllib2

def toggle_hyperioncapture(turnOn):
    api_base_url = 'http://localhost:29445/API'

    if turnOn:
        url = '%s?command=ON' % (api_base_url)
    else:
        url = '%s?command=OFF' % (api_base_url)

    try:
        response = urllib2.urlopen(url)
        response.read()
        pass
    except:
        pass

class Monitor(xbmc.Monitor):
    def __init__(self):
        xbmc.Monitor.__init__(self)

    def onNotification(self, sender, method, data):
        global susppend_auto_change
        global set_for_susspend

        if 'Player.OnStop' in method:
            toggle_hyperioncapture(False)
        if 'Player.OnPlay' in method:
            toggle_hyperioncapture(True)

monitor = Monitor()

# Disable on first start in case Kodi was closed improperly and left it on
toggle_hyperioncapture(False)


while (not xbmc.abortRequested):
    xbmc.sleep(100)
