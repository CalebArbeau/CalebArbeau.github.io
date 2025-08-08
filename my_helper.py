from urllib.request import urlretrieve
import os

def download_file(url, filename):
    try:
        urlretrieve(url, filename)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def getCurPath():
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    path = path.split("FastWindowsSetup2\\scripts")[0] + "FastWindowsSetup2\\"
    return path