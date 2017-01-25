sudo_cmd=$(which sudo)

package1="python2.7"
package2="python-pip"
package3="libqtgui4"
package4="unrar"

if [ -e $sudo_cmd ]; then
	if [ -x /usr/bin/yum ]; then
		sudo yum install $package1 $package2 $package3 $package4
		echo "Yum"
	elif [ -x /usr/bin/apt-get ]; then
		sudo apt-get install $package1 $package2 $package3 $package4
		echo "apt-get"
	elif [ -x /usr/bin/rpm ]; then
		sudo rpm -ivh $package1 $package2 $package3 $package4
	elif [ -x /usr/bin/zypper ]; then
		sudo zypper install $package1 $package2 $package3 $package4
	elif [ -x /usr/bin/pacman ]; then
		sudo pacman -s $package1 $package2 $package3 $package4
	else
		echo "error can't install packages"
		exit 1;
	fi
else
	echo "Please run this script as root or install sudo"
 fi

 mkdir ~/Nexus
 cd ~/Nexus
 pip install --upgrade pip
 wget https://raw.githubusercontent.com/x2110311x/NexusWalletInstaller/master/Source%20Code/Nexus-Linux.py
python Nexus-Linux.py
