---

Created at: 30-06-112011
Last updated at: 30-06-112011
Source URL: http://forum.excito.net/viewtopic.php?f=8&t=1878


---

# forum.excito.net • View topic - Use mobile internet 3g USB dongle as WAN


![http://forum.excito.net/index.php\|220x90](Resources%20+%20Media/attachments/forum.excito.net_•_View_topic_-_Use_mobile_interne.resources/unknown_filename.png)

# [forum.excito.net](http://forum.excito.net)

Excito community forum

 [Advanced search](http://forum.excito.net/search.php)

* [Board index](http://forum.excito.net/index.php) **‹** [Hacking](http://forum.excito.net/viewforum.php?f=15) **‹** [Howtos](http://forum.excito.net/viewforum.php?f=8)

* [Change font size](http://forum.excito.net/viewtopic.php?f=8&t=1878#)
* [Print view](http://forum.excito.net/viewtopic.php?f=8&t=1878&start=0&view=print)

* [FAQ](http://forum.excito.net/faq.php)

* [Register](http://forum.excito.net/ucp.php?mode=register)
* [Login](http://forum.excito.net/ucp.php?mode=login)

## [Use mobile internet 3g USB dongle as WAN](http://forum.excito.net/viewtopic.php?f=8&t=1878&start=0)

[Post a reply](http://forum.excito.net/posting.php?mode=reply&f=8&t=1878)

7 posts • Page **1** of **1**

### [Use mobile internet 3g USB dongle as WAN](http://forum.excito.net/viewtopic.php?f=8&t=1878#p8739)

![http://forum.excito.net/viewtopic.php?p=8739#p8739\|11x9](Resources%20+%20Media/attachments/forum.excito.net_•_View_topic_-_Use_mobile_interne.resources/unknown_filename.1.gif)by **[psykopatpastorn](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2705)** » 27 Jul 2009, 21:35

Disclaimer: no guarantees given. If you brick your unit, tough luck. Anyhow, it works neatly for me. I hope I remember all the steps here.
Being a cheapskate, I have cancelled my ADSL internet and use the mobile internet 3g dongle at home. I get 3-4Mbit/s which is sufficient for my needs. This is how I share the 3g internet connection over my home LAN (and Wifi if you like). The dongle is a Huawei E169 HSDPA USB stick, but it probably works with other dongles too.
If you care about security, start and finish by testing your external firewall (perhaps with some online test like <http://www.auditmypc.com> ).
**\#### Preparation phase:**
1\. stick the dongle into bubba2, let it settle for some seconds
2\. apt-get install wvdial
3\. copy the file contents at the bottom of this message into /etc/wvdial.conf, replacing any existing content
4\. Unless you are using Tre Sweden, edit /etc/wvdial.conf (the INIT3-line and perhaps the PHONE-line is probably enough)
5\. add this to /etc/network/interfaces :

CODE: [SELECT ALL](http://forum.excito.net/viewtopic.php?f=8&t=1878#)
`auto ppp0
iface ppp0 inet wvdial`

6\. unplug your WAN network cable if you have one (as you will temporarily disable the firewall)
7.

CODE: [SELECT ALL](http://forum.excito.net/viewtopic.php?f=8&t=1878#)
`/etc/init.d/bubba-firewall stop
cd /etc/network
cp firewall.conf firewall.conf.orig
sed -i 's/eth0/ppp0/g' firewall.conf`

8\. keep the WAN network cable unplugged, you're switching to 3g wan anyway, and it's not safe as long as you use the modified firewall.conf.
**\#### Test phase:**
1\. type wvdial. It should give you some output and initiate a working internet connection. If not, use the output to debug. 
2\. If it works, send it to background (C-z, then bg) and start the firewall: /etc/init.d/bubba-firewall start
3\. you should now be up and running, and your LAN computers should have internet access
4\. restart your bubba2 if you like to get rid of the terminal emulator used in this test, just to be sure the wvdial won't go down with it.
**\#### Production phase:**
It should all just work now. The ppp0 network interface is set to auto start in /etc/networking/interfaces and the firewall will start as usual, only now using your modified firewall rules. NB: if you switch back to cable WAN, be sure to restore your firewall.conf from the copy you made and restart the firewall.
Well, there it is.
\------ /etc/wvdial.conf --------------

CODE: [SELECT ALL](http://forum.excito.net/viewtopic.php?f=8&t=1878#)
`[Dialer Defaults]
Area Code =
Ask Password = 0
Auto DNS = 1
Baud = 460800
Carrier Check = 0
Compuserve = 0
Dial Command = ATD
DialMessage1 =
DialMessage2 =
Force Address =
ISDN = 0
Idle Seconds = 3000
Init1 = ATZ
Init2 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0
Init3 = AT+CGDCONT=1,"IP","[bredband.tre.se](http://bredband.tre.se)"
Modem = /dev/ttyUSB0
Modem Type = Analog Modem
New PPPD = yes
Password = ;
Phone = *99#
Stupid Mode = 1
Username = ;
`

\------ end of /etc/wvdial.conf ------
Last edited by [psykopatpastorn](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2705) on 29 Jul 2009, 09:27, edited 1 time in total.

[psykopatpastorn](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2705)

**Posts:** 9
**Joined:** 05 Jul 2009, 07:05

[Top](http://forum.excito.net/viewtopic.php?f=8&t=1878#wrap)

### [Re: Use mobile internet 3g USB dongle as WAN](http://forum.excito.net/viewtopic.php?f=8&t=1878#p8742)

![http://forum.excito.net/viewtopic.php?p=8742#p8742\|11x9](Resources%20+%20Media/attachments/forum.excito.net_•_View_topic_-_Use_mobile_interne.resources/unknown_filename.1.gif)by **[carl](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2239)** » 28 Jul 2009, 00:01

There are some places which have "eth0" statically defined; Depending on your needs, you might want to update following files:

* /etc/dhcp3/dhclient-exit-hooks.d/bubba-easyfind

* /etc/dhcp3/dhclient-exit-hooks.d/firewall\_rewrite
* /usr/lib/web-admin/easyfind.pl
* /usr/lib/web-admin/firewall.pl
We have also though of the possibility of using an dongle as WAN, so perhaps we will include such feature as this in the future.
/Carl Fürstenberg, Excito Software Developer
<http://www.excito.com>
[support@excito.com](mailto:support@excito.com)

[carl](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2239)
Site Admin

**Posts:** 399
**Joined:** 07 May 2008, 10:41

[Top](http://forum.excito.net/viewtopic.php?f=8&t=1878#wrap)

### [Re: Use mobile internet 3g USB dongle as WAN](http://forum.excito.net/viewtopic.php?f=8&t=1878#p8743)

![http://forum.excito.net/viewtopic.php?p=8743#p8743\|11x9](Resources%20+%20Media/attachments/forum.excito.net_•_View_topic_-_Use_mobile_interne.resources/unknown_filename.1.gif)by **[psykopatpastorn](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2705)** » 28 Jul 2009, 00:16

> carl wrote:There are some places which have "eth0" statically defined

Thanks for reminding me!

> carl wrote:We have also though of the possibility of using an dongle as WAN, so perhaps we will include such feature as this in the future.

Sounds nice. It would definitely be convenient to have a single WAN interface settings somewhere that controls the whole system.

[psykopatpastorn](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2705)

**Posts:** 9
**Joined:** 05 Jul 2009, 07:05

[Top](http://forum.excito.net/viewtopic.php?f=8&t=1878#wrap)

### [Re: Use mobile internet 3g USB dongle as WAN](http://forum.excito.net/viewtopic.php?f=8&t=1878#p8746)

![http://forum.excito.net/viewtopic.php?p=8746#p8746\|11x9](Resources%20+%20Media/attachments/forum.excito.net_•_View_topic_-_Use_mobile_interne.resources/unknown_filename.1.gif)by **[Harry](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2497)** » 28 Jul 2009, 11:56

> psykopatpastorn wrote:Disclaimer: no guarantees given. If you brick your unit, tough luck. Anyhow, it works neatly for me. I hope I remember all the steps here.
> Being a cheapskate, I have cancelled my ADSL internet and use the mobile internet 3g dongle at home. I get 3-4Mbit/s which is sufficient for my needs. This is how I share the 3g internet connection over my home LAN (and Wifi if you like). The dongle is a Huawei E169 HSDPA USB stick, but it probably works with other dongles too.
> If you care about security, start and finish by testing your external firewall (perhaps with some online test like <http://www.auditmypc.com> ).

Now this sounds really great, especially since I'm really considering buying a 3g router just for this purpose.
Do You have any experiences/theories of hot swapping the 3g dongle? which would come in handy if I would like to use the 3g dongle out in the field on a regularly frequent basis.
I wonder if I could use my Iphone as a 3g "dongle" for the above? It works great as a 3g "dongle" on an Windows xp PC.
Cheers
Harry

[Harry](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2497)

**Posts:** 20
**Joined:** 12 Feb 2009, 16:43

[Top](http://forum.excito.net/viewtopic.php?f=8&t=1878#wrap)

### [Re: Use mobile internet 3g USB dongle as WAN](http://forum.excito.net/viewtopic.php?f=8&t=1878#p8748)

![http://forum.excito.net/viewtopic.php?p=8748#p8748\|11x9](Resources%20+%20Media/attachments/forum.excito.net_•_View_topic_-_Use_mobile_interne.resources/unknown_filename.1.gif)by **[psykopatpastorn](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2705)** » 28 Jul 2009, 13:10

> Harry wrote:especially since I'm really considering buying a 3g router just for this purpose.

I did too, before I realised I should buy a Bubba2 instead. A bit more expensive, but of course you get so much more than a 3g router for the money. Also, I don't trust the 3g router firewall. With iptables, I can see what's going on.

> Harry wrote:Do You have any experiences/theories of hot swapping the 3g dongle? which would come in handy if I would like to use the 3g dongle out in the field on a regularly frequent basis.

You mean you want to jerk it out of your bubba2 while it's up and running, and then stick it back in and hope everything will work? I doubt that will work, mostly because wvdial will get an interrupted session, and you don't have anything that will reinitiate it upon re-insertion of the dongle. The risk of hardware or OS damage is minimal (or non-existant even?) though. What I would recommend, is to shut down the bubba, then disattach the dongle. When you get back home, you re-insert the dongle, then boot up the bubba.

> Harry wrote:I wonder if I could use my Iphone as a 3g "dongle" for the above? It works great as a 3g "dongle" on an Windows xp PC.

I don't know. Do you connect it to the PC with a usb cable, or is it bluetooth? My intuition says it won't work out of the box, prepare for some configuration.

[psykopatpastorn](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2705)

**Posts:** 9
**Joined:** 05 Jul 2009, 07:05

[Top](http://forum.excito.net/viewtopic.php?f=8&t=1878#wrap)

### [Re: Use mobile internet 3g USB dongle as WAN](http://forum.excito.net/viewtopic.php?f=8&t=1878#p8822)

![http://forum.excito.net/viewtopic.php?p=8822#p8822\|11x9](Resources%20+%20Media/attachments/forum.excito.net_•_View_topic_-_Use_mobile_interne.resources/unknown_filename.1.gif)by **[psykopatpastorn](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2705)** » 07 Aug 2009, 07:45

I ran into this trouble every 1440 minutes:

CODE: [SELECT ALL](http://forum.excito.net/viewtopic.php?f=8&t=1878#)
`Aug  6 11:05:18 bubba pppd[4297]: LCP terminated by peer
Aug  6 11:05:18 bubba pppd[4297]: Connect time 1440.0 minutes.
Aug  6 11:05:18 bubba pppd[4297]: Sent 18690882 bytes, received 226028192 bytes.
Aug  6 11:05:18 bubba pppd[4297]: Modem hangup
Aug  6 11:05:18 bubba pppd[4297]: Connection terminated.
`

I don't know whether it's actually peer who terminates the connection, or it's because of some session timeout setting in wvdial/ppp/?, but if you add this line to wvdial.conf, it will reconnect automatically:

CODE: [SELECT ALL](http://forum.excito.net/viewtopic.php?f=8&t=1878#)
`Auto Reconnect = On
`

There is still one disconnection problem left, which happens more rarely, and which does not seem recoverable by wvdial. Judging from the syslog, it seems like the USB-dongle itself drops out. Then it is rediscovered, and the fake CD-rom-partition (used by the stick for auto-running stuff in Windows) is mounted again, and the modem is reattached to ttyUSB0. By then, though, wvdial seems to have given up on the modem.

[psykopatpastorn](http://forum.excito.net/memberlist.php?mode=viewprofile&u=2705)

**Posts:** 9
**Joined:** 05 Jul 2009, 07:05

[Top](http://forum.excito.net/viewtopic.php?f=8&t=1878#wrap)

### [Re: Use mobile internet 3g USB dongle as WAN](http://forum.excito.net/viewtopic.php?f=8&t=1878#p14562)

![http://forum.excito.net/viewtopic.php?p=14562#p14562\|11x9](Resources%20+%20Media/attachments/forum.excito.net_•_View_topic_-_Use_mobile_interne.resources/unknown_filename.1.gif)by **[Lars akerman](http://forum.excito.net/memberlist.php?mode=viewprofile&u=3355)** » 08 Apr 2011, 19:04

Hi,
I tried the guide using my Bubba 2 Wifi and a Huawei e1750 with no success.
I get the following error message:
Cannot open /dev/ttyUSB0: No such file or directory
Anyone know what might be wrong?
I then found the following guide:
<http://www.geeksonhigh.com/tag/usb-modeswitch>
But it was not able to find and install the "usb-modeswitch" on my bubba 2. Anyone know if this can be done?
I found the "usb-modeswitch" package for Debian Squeeze but not for Debian Etch. Will a Debian Squeeze firmware upgrade soon be available for Bubba 2?
[http://packages.debian.org/search?keywo ... modeswitch](http://packages.debian.org/search?keywords=usb-modeswitch)
Thanks
Lars

[Lars akerman](http://forum.excito.net/memberlist.php?mode=viewprofile&u=3355)

**Posts:** 7
**Joined:** 08 Apr 2011, 15:18

[Top](http://forum.excito.net/viewtopic.php?f=8&t=1878#wrap)

Display posts from previous: All posts1 day7 days2 weeks1 month3 months6 months1 year Sort by AuthorPost timeSubject AscendingDescending 

* * *

[Post a reply](http://forum.excito.net/posting.php?mode=reply&f=8&t=1878)

7 posts • Page **1** of **1**

[Return to Howtos](http://forum.excito.net/viewforum.php?f=8)

Jump to: Select a forum------------------General   Announcements   Feedback   TestBubba Two & Excito B3   B2 & B3 Support   B2 & B3 Feature Requests   My BubbaBubba Server (AKA Bubba 1)   Bubba Server Support   Bubba Server Feature requests   My Bubba ServerHacking   Howtos   Development 

### WHO IS ONLINE

Users browsing this forum: No registered users and 1 guest

* [Board index](http://forum.excito.net/index.php)

* [The team](http://forum.excito.net/memberlist.php?mode=leaders) • [Delete all board cookies](http://forum.excito.net/ucp.php?mode=delete_cookies) • All times are UTC + 1 hour \[ DST \]

Powered by [phpBB](http://www.phpbb.com/) © 2000, 2002, 2005, 2007 phpBB Group

