cd C:\
mkdir Nexus
cd Nexus
IF NOT EXIST C:\Python27 (
bitsadmin /transfer PythonDownload /download /priority normal https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi C:\Nexus\python.msi
python.msi
) ELSE (
echo "Python Already Installed")
bitsadmin /transfer NexusInstaller /download /priority normal https://raw.githubusercontent.com/x2110311x/NexusWalletInstaller/master/Nexus.py C:\Nexus\nexus.py
cd C:\Python27
python C:\Nexus\nexus.py
pause
exit