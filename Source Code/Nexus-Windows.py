import os
os.system('python -m pip install rarfile')
os.system('python -m pip install clint')
os.system('python -m pip install requests')
import requests
import distutils.dir_util
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
				
#Create File and Folder 
HomeFolder	 = os.path.expanduser("~")
WalletFolder = HomeFolder + '\\Nexus'
WalletRar = HomeFolder + '\\nexus.rar'
DatabaseRar = HomeFolder + "\\AppData\\Roaming\\Nexus\\Database.rar"
DatabaseFolder = HomeFolder + "\\AppData\\Roaming\\Nexus\\"
WalletFolder = WalletFolder + "\\Nexus 2.2.3 - LLD Stable - Win x64 - build 01-09-17"
		
#Download Files and Extract
download('http://nexusearth.com/wallet/2.2.3/Nexus-Qt.rar', WalletRar, "Wallet") #Download Wallet From NexusEarth
download('https://transfer.sh/N6xts/unrar.exe',"C:\Python27\unRAR.exe", "UnRar") #Download Unrar to extract Walletdistutils.dir_util.mkpath(WalletFolder)
WalletRar = rarfile.RarFile(WalletRar)
rarfile.UNRAR_TOOL = "C:\Python27\unRAR.exe"
WalletRar.extractall(WalletFolder)
download('http://nexusearth.com/bootstrap/LLD-Database/recent.rar',DatabaseRar, "Bootstrap Database") #Download Bootstrap Database
DatabaseRar = rarfile.RarFile(DatabaseRar)
DatabaseRar.extractall(DatabaseFolder)
		
print "Nexus Wallet Installed in %s" % WalletFolder
print "Press Enter To Quit"
raw_input()