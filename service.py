# -*- coding: utf-8 -*-
import os
import urllib2
import xbmc

lock_file = 'hyperion.lock'

def toggle_hyperioncapture(turnOn, force = False):
    api_base_url = 'http://localhost:29445/API'

    if turnOn:
        url = '%s?command=ON&force=%s' % (api_base_url, force)
    else:
        url = '%s?command=OFF&force=%s' % (api_base_url,force)

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

        # If no lock file exists handle command
        if not os.path.exists(lock_file):
          if 'Player.OnStop' in method:
              xbmc.log('[hyperionscreencapture] player stopped, disabling hyperionscreencapture', xbmc.LOGDEBUG)
              toggle_hyperioncapture(False)
          if 'Player.OnPlay' in method:
              xbmc.log('[hyperionscreencapture] player started, enabling hyperionscreencapture', xbmc.LOGDEBUG)
              toggle_hyperioncapture(True)
          if 'Player.OnPause' in method:
            pass

monitor = Monitor()

# Disable on first start in case Kodi was closed improperly and left it on
toggle_hyperioncapture(False, True)


while (not xbmc.abortRequested):
    xbmc.sleep(100)
