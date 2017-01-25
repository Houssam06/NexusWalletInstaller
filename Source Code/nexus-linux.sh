yum_cmd=$("which yum")
apt-cmd=$(which apt-get)
rpm_cmd=$(which rpm)
zypper_cmd=$(which zypper)
pacman_cmd=$(which pacman)
sudo_cmd=$(which sudo)

package1="python2.7"
package2="python-pip"
package3="libqtgui4"
package4="unrar"

if [[ ! -e $sudo_cmd ]]; then
	if [[ ! -e $yum_cmd ]]; then
		sudo yum install $package1 $package2 $package3 $package4
	elif [[ ! -e $apt_cmd ]]; then
		sudo apt-get install $package1 $package2 $package3 $package4
	elif [[ ! -e $rpm_cmd ]]; then
		sudo rpm -ivh $package1 $package2 $package3 $package4
	elif [[ ! -e $zypper_cmd ]]; then
		sudo zypper install $package1 $package2 $package3 $package4
	elif [[ ! -e $pacman_cmd ]]; then
		sudo nepacman -s $package1 $package2 $package3 $package4
	else
		echo "error can't install packages"
		exit 1;
	fi
else
	echo "Please run this script as root or install sudo"
 fi
 
 mkdir ~/Nexus
 cd ~/Nexus
 wget https://raw.githubusercontent.com/x2110311x/NexusWalletInstaller/master/Source%20Code/Nexus-Linux.py
 python Nexus-Linux.
