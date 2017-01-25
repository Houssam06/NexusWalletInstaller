import os
#os.system('python -m pip install tarfile')
os.system('python -m pip install rarfile')
os.system('python -m pip install clint')
os.system('python -m pip install requests')
import requests
import distutils.dir_util
#import tarfile
import rarfile
from clint.textui import progress

def download(url, path, file):		
	r = requests.get(url, stream=True)
	print "Downloading %s" %file
	with open(path, 'wb') as f:
		total_length = int(r.headers.get('content-length'))
		for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
			if chunk:
				f.write(chunk)
				f.flush()

#Create File and Folder Variables
HomeFolder = os.path.expanduser("~")
WalletRar = HomeFolder + '/nexus.tgz'
WalletFolder = HomeFolder + "/Nexus"
DatabaseFolder = HomeFolder + "/.Nexus"
DatabaseRar = HomeFolder + "/nexus.rar"
	
download('http://nexusearth.com/wallet/2.2.3/Nexus-Qt.tgz', WalletRar, "Wallet")
WalletTar= tarfile.open(WalletRar)
WalletTar.extractall(path=WalletFolder)
WalletTar.close()
rarfile.UNRAR_TOOL = "/usr/bin/unrar"
download('http://nexusearth.com/bootstrap/LLD-Database/recent.rar', DatabaseRar , "Bootstrap Database") #Download Bootstrap Database
DatabaseRar = rarfile.RarFile(DatabaseRar)
DatabaseRar.extractall(DatabaseFolder)
	
print "Nexus Wallet Installed to %s" %WalletFolder
print "Press Enter To Quit"
raw_input()
quit()
