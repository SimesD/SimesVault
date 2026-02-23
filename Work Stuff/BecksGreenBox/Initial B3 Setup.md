---

Created at: 24-06-112011
Last updated at: 04-07-112011


---

# Initial B3 Setup


Administrator
b3cksgr33n

becksgreen
greenbecks

Workgroup becksgreen
host becks1uk.local (becks(n)(UK).local

Install procedure
update OS
change admin password
Create user becksgreen
setup wifi

Packages to install
apt-get install PPP
apt-get install usbutils
apt-get install ftp

experimenting with bridge and dnsmasq Replace when final

Country specific versions

UK
becksgreen1   

Wvial backup connection method

wvdial- no longer needed with new pon/poff

Problem now solved, Carl compiled a new vwdial package for you (actually the dependency wvstream was the issue). 
If you change sources to our vincent repo (do, as root, 'change\_distribution vincent') and apt-get install wvdial you should be fine. 
After changing source do apt\_get update
Don't forget to reset the sources list to original settings before doing other installs (or updates), vincent is our testing repo. 

Change back to change\_distribution elvin

once installed use dial wvdial.conf:-

**<u>UK-3 ZTEmodems</u>**

\[Dialer Defaults\]

Modem = /dev/ttyUSB2

ISDN = off

Modem Type = USB Modem

Baud = 7200000

Init = ATZ

Init2 =AT+CGDCONT=1,"IP","[three.co.uk](http://three.co.uk)" 

Init3 = 

Init4 = 

Init5 = 

Init6 = 

Init7 = 

Init8 = 

Init9 = 

Phone = \*99#

Phone1 = 

Phone2 = 

Phone3 = 

Phone4 = 

New PPPD = yes

Dial Prefix = 

Dial Attempts = 1

Dial Command = ATM1L3DT

Ask Password = off

Password = off

Username = na

Auto Reconnect = on

Abort on Busy = off

Carrier Check = off

Check Def Route = on

Abort on No Dialtone = off

Stupid Mode = on

Idle Seconds = 0

Auto DNS = off

check DNS = off

etc/network/interfaces

cp original to etc/network/interfaces.orig

