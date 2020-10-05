#!/usr/bin/env python3

'''A simple deployment script for new CentOS 8 Setup'''
###########
# Imports #
###########

import getpass
import os
import sys


#############
# Variables #
#############

choice = False
audoconnect = True


#############
# Functions #
#############


def print_conf(hostname,domain,fqdn,ipaddr,mask,dns1,dns2,dnsservers,username,interface):
    print("")
    print("To be Configured:")
    print("Short Hostname: " + hostname)
    print("Domain Name: " + domain)
    print("FQDN: " + fqdn)
    print("IP Address: " + ipaddr + "/" + str(mask))
    print("DNS Server #1: " + dns1)
    print("DNS Server #2: " + dns2)
    print("Interface to modify: " + interface)
    print("Username: " + username)
    print("Domain to Join: " + domain)
    print("Password is intentially not shown.")
    print("")


def prompt_sys_info():
    print("")
    print("Please provide all of the following information")
    print("")
    fqdn = input("Please input the desired FQDN for this system. Please ensure that the domain is a valid and reachable domain using Active Directory: ")
    ipaddr = input("Please input the desired IP Address: ")
    mask = input("Please input the desired netmask in short notation (default. 24): ").format(int) or int(24)
    gateway = input("Plese input the desired gateway IP Address: ")
    dns1 = input("Enter the first DNS Server to use (IP): ")
    dns2 = input("Enter the second DNS Server to use (IP): ")
    dnsservers = dns1 + "," + dns2
    username = input("Enter a username that has the ability to join the system to the domain: ")
    print("Valid Interfaces:")
    print(os.system('nmcli c show'))
    interface = input("Select Interface to configure with the above information: ")
    hostname = fqdn.split('.')[0] 
    _domain = fqdn.split('.')[1:]
    domain = '.'.join(_domain)
    return (hostname,domain,fqdn,interface,ipaddr,mask,dns1,dns2,dnsservers,username)


def test_network(ipaddr, gateway, dns1, dns2, domain):
    print('Ping test to local interface')
    print(os.system('ping -c 4 ' + ipaddr))
    print('Ping test to gateway')
    print(os.system('ping -c 4 ' + gateway))
    print('Ping/DNS test to DNS Server #1')
    print(os.system('ping -c 4 ' + dns1))
    print(os.system('dig ' + domain + ' @' + dns1))
    print('Ping/DNS test to DNS Server #2')
    print(os.system('ping -c 4 ' + dns2))
    print(os.system('dig ' + domain + ' @' + dns2))
    

def query_yes_no(question, default="no"):
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def net_conf(ipaddr, gateway, dns1, dns2, hostname, domain, interface):
    print('Configuring hostname')
    system.os('hostnamectl set-hostname ' + hostname)
    print('Configuring network interface ' + interface)



##################
# Main Execution #
##################

# Prompt for user input for system information as long as the confirmation is "No"
while not choice:
    sys_conf = prompt_sys_info()
    print_conf(sys_conf)
    choice = query_yes_no("Does the above information look correct?")
    if choice:
        break
    elif not choice:
        continue


if choice:
    print ("")
    print ("Great, we'll go ahead and proceed with the setup now.")
    print ("")
else:
    print("Something went wrong and we got an unexpected result from your confirmation. If you believe this is a bug, please report it to the github!")
    raise ValueError

# Setting Autoconnect Preference
if autoconnect:
    autoconnect = "yes"
else:
    autoconnect = "no"
# Configuring Network Interface
print('Configuring network interface ' + )
os.system('nmcli c mod ' + interface + ' connection.autoconnect ' + autoconnect + 
          ' ipv4.address ' + ipaddr + ' ipv4.gateway ' + gateway + ' ')

'''
# User Confirmation
print("")
print("Please validate that the information below is correct, then press y/n to proceed with configuration [Yy] or exit the script [Nn]")
print("")

print("")
print("Are the above items correct (y/n)?")

_response = askuser()
if _response == True:
    print("")
    print("Proceeding to configuration")
    print("")
else:
    print("")
    print("Response was no, re-prompting for input")
    sys.exit(1)
'''
