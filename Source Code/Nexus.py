#Python Script to automatically install Nexus

#Install Needed Modules
import os
import platform
OS = platform.system()
if OS == "Linux":
	os.system("sudo apt-get -f  install python-pip")
	os.system("sudo apt-get -f install libqtgui4") #Install LibQTGUI if not installed. Most likely will need sudo password
os.system('python -m pip install rarfile')
os.system('python -m pip install clint')
os.system('python -m pip install requests')

	# Import Necessary Libraries
import requests
import distutils.dir_util
import rarfile
import tarfile
from clint.textui import progress
import zipfile

#Define Functions
			
def download(url, path, file):		
	r = requests.get(url, stream=True)
	print "Downloading %s" %file
	with open(path, 'wb') as f:
		total_length = int(r.headers.get('content-length'))
		for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
			if chunk:
				f.write(chunk)
				f.flush()

#Download Nexus Wallet
HomeFolder	 = os.path.expanduser("~")
if OS == "Linux": #If OS is Linux
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
		
if OS == "Windows": #If OS is Windows 
		
	#Create File and Folder Variables
	WalletFolder = HomeFolder + '\\Nexus'
	WalletRar = 'C:\\Nexus\\nexus.rar'
	DatabaseRar = "C:\\Nexus\\database.rar"
	DatabaseFolder = HomeFolder + "\\AppData\\Roaming\\Nexus\\"
	WalletFolder = WalletFolder + "\\Nexus 2.2.3 - LLD Stable - Win x64 - build 01-09-17"
		
	#Download Files and Extract
	download('http://nexusearth.com/wallet/2.2.3/Nexus-Qt.rar', WalletRar, "Wallet") #Download Wallet From NexusEarth
	download('https://transfer.sh/N6xts/unrar.exe',"C:\Python27\unRAR.exe", "UnRar") #Download Unrar to extract Wallet
	distutils.dir_util.mkpath(WalletFolder)
	WalletRar = rarfile.RarFile(WalletRar)
	rarfile.UNRAR_TOOL = "C:\Python27\unRAR.exe"
	WalletRar.extractall(WalletFolder)
	download('http://nexusearth.com/bootstrap/LLD-Database/recent.rar',DatabaseRar, "Bootstrap Database") #Download Bootstrap Database
	DatabaseRar = rarfile.RarFile(DatabaseRar)
	DatabaseRar.extractall(DatabaseFolder)
		
	print "Nexus Wallet Installed in %s" % WalletFolder
	print "Press Enter To Quit"
	raw_input()
#Cleaning Up
print "Cleaning Up"
os.system('python -m pip uninstall rarfile')
os.system('python -m pip uninstall clint')
os.system('python -m pip uninstall requests')
quit()