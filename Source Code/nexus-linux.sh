yum_cmd=$(which yum)
apt-cmd=$(which apt-get)
rpm_cmd=$(which rpm)
zypper_cmd=$(which zypper)
pacman_cmd=$(which pacman)

package1="python2.7"
package2="python-pip"
package3="libqtgui4"
package4="unrar"

if [[ ! -z $yum_cmd ]]; then
    yum install $package1 $package2 $package3 $package4
 elif [[ ! -z $apt_cmd ]]; then
    apt-get install $package1 $package2 $package3 $package4
 elif [[ ! -z $rpm_cmd ]]; then
	rpm -ivh $package1 $package2 $package3 $package4
 elif [[ ! -z $zypper_cmd ]]; then
	zypper install $package1 $package2 $package3 $package4
 elif [[ ! -z $pacman_cmd ]]; then
	pacman -s $package1 $package2 $package3 $package4
 else
    echo "error can't install packages"
    exit 1;
 fi
 
 mkdir ~/Nexus
 cd ~/Nexus
 wget https://raw.githubusercontent.com/x2110311x/NexusWalletInstaller/master/Source%20Code/Nexus-Linux.py
 python Nexus-Linux.py
