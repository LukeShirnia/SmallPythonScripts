#!/usr/bin/python
import platform
import sys
# does not currently work as expected on RHEL/CENTOS 5

supported_centos = [6, 7]
supported_ubuntu = [12, 14, 16]
CentOS_RedHat_Distro = ['redhat', 'centos', 'red', 'red hat']
Ubuntu_Debian_Distro = ['ubuntu', 'debian']

def os_check():
        os_platform = platform.system()
        if os_platform == "Linux":
                distro = platform.linux_distribution()[0]
                distro = distro.split()[0]
                return distro
        else:
                print "Stop Using a Rubbish OS!!"

os_check_value = os_check()
if os_check_value.lower() in CentOS_RedHat_Distro:
        print "RedHat"
elif os_check_value.lower() in Ubuntu_Debian_Distro:
        print "Ubuntu"
else:
        print "OS Not Recognised"
