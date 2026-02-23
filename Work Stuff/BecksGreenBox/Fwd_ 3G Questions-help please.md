---

Created at: 01-07-112011
Last updated at: 01-07-112011


---

# Fwd: 3G Questions-help please


Begin forwarded message:

> **From:** Carl Fürstenberg <[carl@excito.com](mailto:carl@excito.com)\>
> 
> **Date:** 1 July 2011 10:52:41 GMT+01:00
> 
> **To:** Simon Davies <[simon@visim.tv](mailto:simon@visim.tv)\>
> 
> **Cc:** Johannes Book <[johannes.book@excito.com](mailto:johannes.book@excito.com)\>
> 
> **Subject:** **Re: 3G Questions-help please**
> 
> 2011-07-01 00:24, Simon Davies skrev:
> 
> > Hi Carl,
> 
> Hi Simons,
> 
> > I am having problems following what is going on in the network config in the B3
> 
> I hope we can fix this for you.
> 
> > I have tried modifying the firewall.conf file but this gets overwritten on reboot.
> 
> During boot, the file /etc/network/firewall.conf will be read, thus you
> need to save the current firewall there, i.e. "iptables-save >
> /etc/network/firewall.conf"
> 
> > Is there any way to turn off all of the B3 network management so that I can do my own network config.
> 
> The B3 network config is read by the init script bubba-firewall; you can
> disable that by issuing the command "update-rc.d bubba-firewall remove".
> Also the files
> /etc/dhcp/dhclient-exit-hooks.d/firewall\_rewrite and
> /etc/dhcp/dhclient-exit-hooks.d/bubba-easyfind is relevant for WAN
> (either remove firewall\_rewrite and/or change eth0 to ppp0)
> 
> > 
> 
> > Or perhaps you can suggest where to look. I am going to try a bridge from ppp0 > eth0 to see of that works
> 
> I'm sorry, but I was wrong before when suggesting you to bridge the
> interfaces, which is only relevant for LAN type of networks.
> 
> > The configuration need to achieve Is quite simple:-
> 
> > 
> 
> > Internet access will be provided by a 3G connection on ppp0
> 
> If there will always only be an ppp0 connection, and never an eth0 WAN
> connection, one alternative is actually to change all instances of eth0
> in B3 to ppp0, the only thing that needs to take into account is that
> the ppp0 interface is up and running at the right™time :)
> There are still some hard coded references to eth0 in the packages
> bubba-frontend and bubba-backend, but you could try changing them to
> ppp0 and rebuild the packages (see
> <http://wiki.excito.org/wiki/index.php/Tutorials_and_How-tos/Build_Packages>
> for an howto).
> In other cases, I've tried to abstract all references to wan and lan
> interfaces into the bubba-networkmanager package, which that handles
> network config related settings, inclusing what is WAN and LAN. It uses
> the config file /etc/bubba-networkmanager.conf to save and read what is
> currently specified.
> 
> > This will be used for refreshing content on the server I will need to use the myownb3 service to locate the servers over the 3g connection.
> 
> /etc/dhcp/dhclient-exit-hooks.d/bubba-easyfind will need to be updated
> so easyfind will trigger over the ppp0 interface instead of the eth0
> interface.
> 
> > mobile devices connect to the b3 and stream content via WiFi from shared folders on the B3.
> 
> > 
> 
> > Mobile devices connected to WiFi will only be allowed to connect to the streamed content on the server and possibly to becks.com
> 
> That should be possible using iptables, and possible some other proxy
> software, depending on how strict the filtering should be.
> 
> > 
> 
> > Also can you give me some guidance on how to compile my own install image so tha it can dploy my config on to all 20 devices easily.
> 
> We have some scripts we are using for building the images, Though I need
> to talk to management before I can supply you with them.
> 
> > You support would be appreciated.
> 
> > 
> 
> > Simon
> 
> > 
> 
> > +447973225418
> 
> > simon@visim.tv
> 
> > 
> 
> > 
> 
> I hope this information is somewhat useful for you; Don't hesitate to
> call me again if you have more questions.
> Regards,
> Carl Fürstenberg - Excito Electronics

Simon Davies
[simon@visim.tv](mailto:simon@visim.tv)
+447973225418

