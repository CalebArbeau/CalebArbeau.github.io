import my_helper
from time import sleep
import os

def download(sender, app_data, url):
    if (not url):
        url = 'https://l.netnda.io/'
    my_helper.download_file(url, "programs\\syncro.exe")
    
    time = 0
    while (not os.path.exists("programs\\syncro.exe") and not time >= 5) :
        time = time + 1
        sleep(1)
        pass
    if (time == 5):
        print("Couldn't download syncro")
    else:
        install()

def install():
    path = my_helper.getCurPath() + "programs\\syncro.exe"
    print("Opening " + path)
    open(path)