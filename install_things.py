import os

def install_things():
    os.system('sudo pip install --upgrade youtube_dl')
    os.system('sudo apt-get install libgnome2-0')




if __name__ == '__main__':
    install_things()
