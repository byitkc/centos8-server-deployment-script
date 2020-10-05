# CentOS 8 Deployment Script

This is a script that I use on my internal systems to provision them after cloning from a VMware teamplate. It requires python3.

The following actions are taken by this deployment script.

1. Prompt for User Input for all required fields
2. Re-generate host SSH keys
3. *WIP*: Configure Hostname of Server
4. *WIP*: Configure Network settings per use input
5. *WIP*: Test Network by pinging and attempt DNS resolution of the domain
6. *WIP*: Join the system to an AD Domain
7. *WIP*: Modify /etc/sssd/sssd.conf to not require the domain name be defined
8. *WIP*: Configure /etc/sudoers.d/domain to allow the 