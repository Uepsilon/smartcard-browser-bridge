import subprocess

def openBrowser(url):
    print "Opening URL: "+ url
    openBrowserCmd = "DISPLAY=:0 chromium-browser --kiosk --disable-session-crashed-bubble --noerrdialogs %s" % url
    subprocess.Popen(openBrowserCmd, shell=True)
