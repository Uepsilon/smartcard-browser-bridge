import os

class browserHandler(object):
    browserURL = None;
    def __init__(self, url):
        self.browserURL = url
        open()

    def open(self):
        openBrowserCmd = "chromium-browser --kiosk --disable-session-crashed-bubble --noerrdialogs" + self.browserURL
        os.cmd(openBrowserCmd)
