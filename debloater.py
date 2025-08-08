import os
import shutil
import zipfile
import my_helper

def qdebloat():
    url = "https://github.com/Raphire/Win11Debloat/archive/master.zip"
    my_helper.download_file(url, "programs\\debloat.zip")
    
    while (not os.path.exists("programs\\debloat.zip")) :
        pass
    
    with zipfile.ZipFile("programs\\debloat.zip","r") as zip_ref:
            zip_ref.extractall("programs")
    os.remove("programs\\debloat.zip")

def remove_debloater():
    shutil.rmtree("programs\\Win11Debloat-master", ignore_errors=True)