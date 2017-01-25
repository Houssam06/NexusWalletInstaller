import os


os.system("sudo apt-get -f  install python-pip")
os.system("sudo apt-get -f install libqtgui4")
os.system('python -m pip install tarfile')
os.system('python -m pip install clint')
os.system('python -m pip install requests')
import requests
import distutils.dir_util
import tarfile
from clint.textui import progress

#Have User Confirm
print "Note This Only Works on Debian-Based Distros"
print "You may need to install some packages, so be ready to enter sudo password and enter \"y\""
print "Press Enter to Continue"
raw_input()
#Create File and Folder Variables
WalletRar = HomeFolder + '//nexus.tgz'
WalletFolder = HomeFolder + "//Nexus"
DatabaseFolder = HomeFolder + "//.Nexus"
DatabaseRar = HomeFolder + "//nexus.rar"
	
download('http://nexusearth.com/wallet/2.2.3/Nexus-Qt.tgz', WalletRar, "Wallet")
WalletTar= tarfile.open(WalletRar)
WalletTar.extractall(path=WalletFolder)
WalletTar.close()
os.system("sudo apt-get install unrar")
rarfile.UNRAR_TOOL = "/usr/bin/unrar"
download('http://nexusearth.com/bootstrap/LLD-Database/recent.rar', DatabaseRar , "Bootstrap Database") #Download Bootstrap Database
DatabaseRar = rarfile.RarFile(DatabaseRar)
DatabaseRar.extractall(DatabaseFolder)
	
print "Nexus Wallet Installed to %s" %WalletFolder
print "Press Enter To Quit"
raw_input()
quit()
