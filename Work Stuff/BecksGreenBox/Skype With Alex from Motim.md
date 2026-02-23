---

Created at: 12-07-112011
Last updated at: 12-07-112011


---

# Skype With Alex from Motim


\[11/07/2011 06:17:23\] SimonD: Authorization granted to Alexander Gee
\[11/07/2011 06:17:32\] Alexander Gee: Good morning
\[11/07/2011 06:17:54\] SimonD: Hi Alex!
\[11/07/2011 06:18:00\] Alexander Gee: I've just added your two NYC locations
\[11/07/2011 06:18:14\] SimonD: Will send you a location at the Hotel where I am working
\[11/07/2011 06:18:23\] SimonD: OK Where?
\[11/07/2011 06:18:34\] Alexander Gee: 40.76454628629767, -73.99592936038971 (real box - Kate)
40.7694592948433, -74.00442123413086 (Virtual box - Arne Quinze)
\[11/07/2011 06:18:44\] Alexander Gee: Hopefully those are the ones you sent us
\[11/07/2011 06:18:56\] Alexander Gee: If you need another I can pop that in too
\[11/07/2011 06:19:12\] SimonD: Ok let me check
\[11/07/2011 06:23:45\] SimonD: just sent you a location
\[11/07/2011 06:23:57\] SimonD: From google
\[11/07/2011 06:24:06\] Alexander Gee: Yup it just appeared
\[11/07/2011 06:24:06\] SimonD: Thats where I am now
\[11/07/2011 06:24:51\] Alexander Gee: I assume you would like a virtual box?
\[11/07/2011 06:25:15\] SimonD: Yup no real boxes here that I can see :-)
\[11/07/2011 06:25:43\] Alexander Gee: Ok cool, I'm doing one now
\[11/07/2011 06:25:50\] SimonD: Authorization granted to Alexander Gee
\[11/07/2011 06:26:53\] Alexander Gee: You won't need this placement more than say a week will you?
\[11/07/2011 06:27:16\] SimonD: No I am gone from NY tonight
\[11/07/2011 06:27:23\] Alexander Gee: Ok cool
\[11/07/2011 06:27:33\] Alexander Gee: In that case you are all set
\[11/07/2011 06:27:37\] Alexander Gee: Should be there now
\[11/07/2011 06:28:33\] SimonD: Ok jus need to get the app installed, I am going to blow the ipad away and start with a clean install
\[11/07/2011 06:29:00\] SimonD: Let me know when you want to go through [rsync.net](http://rsync.net)
\[11/07/2011 06:29:40\] Alexander Gee: Cheers, I've got a few more things to hit first I'll ping you when I'm up to it.
\[11/07/2011 06:31:20\] Alexander Gee: Oh actually can you fire me that UDID if you have it handy, I'm just going to check its in (might as well it can't hurt)
\[11/07/2011 06:31:34\] SimonD: ok will do
\[11/07/2011 06:32:40\] SimonD: OK Sent my UDID let me know...
\[11/07/2011 06:33:11\] Alexander Gee: Thanks I'll get back to your shortly
\[11/07/2011 06:36:55\] Alexander Gee: Ok that UDID is definately in our build
\[11/07/2011 06:38:04\] SimonD: ok rsyncing my ipad now will let you know how it goes
\[11/07/2011 06:38:21\] Alexander Gee: Excellent
\[11/07/2011 07:27:58\] Alexander Gee: Hey Simon I've just hit a stall on my other tasks so now would be a great time to talk about rsync if you are free
\[11/07/2011 07:28:48\] SimonD: OK Ipad is still backing up syncing etc so still waiting for that.
\[11/07/2011 07:29:46\] SimonD: OK , so rsyn.cnet has a load of help on how to set it up. But essentially tou can connect or sync from pretty much anything.
\[11/07/2011 07:30:59\] SimonD: I am using a custom debian linux build and using rsync but your can use a pac mac or whatever to connect with the service using rsyn, sftp, scp etc.
\[11/07/2011 07:31:32\] SimonD: Where are your files hosted ater you have qA them and have them ready for release?
\[11/07/2011 07:32:22\] Alexander Gee: They are up in a web accessable directory on our VPS. Unfortunately currently test files are also in the same directory.
\[11/07/2011 07:34:15\] SimonD: OK we I guess the easiet way to manage it would be to have a release directory and then eiher manually place or automatically sync to my sync directory.
\[11/07/2011 07:35:30\] Alexander Gee: At the moment I'll have to do it manually since I can't tinker too much right at the moment. Do you have a windows client you'd reccomend?
\[11/07/2011 07:37:47\] SimonD: OK, you can set it up as a webdav folder or use sftp/scp client. probably winscp?
\[11/07/2011 07:38:00\] SimonD: <http://winscp.net/eng/index.php>
\[11/07/2011 07:38:47\] SimonD: i dont use windows pcs that much but winscp did the job pretty well last time I used it.
\[11/07/2011 07:39:33\] Alexander Gee: Excellent. I'm kind of stuck with them for this project since we decided on [ASP.NET](http://ASP.NET) not that I'm much of a linux user these days
\[11/07/2011 07:42:06\] SimonD: OK, So if you set up winscp then put a test file there we can check the process through. Content directory target for you is here here <http://usw-s007.rsync.net/becksgreen/>
\[11/07/2011 07:43:27\] SimonD: try these instructions first and let me know when you have put a test file there
\[11/07/2011 07:43:31\] SimonD: Further, your [rsync.net](http://rsync.net) filesystem is accessible over WebDAV via URL in this format:
webdavs://usw-s007.[rsync.net/The](http://rsync.net/The) trailing '/' at the end of the URL is required.  Windows XP and Mac OSX WebDAV clients
(such as the Finder) may require slightly different syntax, such as:
<https://usw-s007.rsync.net/>
\[11/07/2011 07:44:00\] SimonD: webdav is built into windows I think
\[11/07/2011 08:06:49\] Alexander Gee: Sorry I tried the webdav path with windows and... no luck it needs many patches to make the windows client work.
\[11/07/2011 08:07:10\] Alexander Gee: So I went to winscp and it was done in 5 minutes, you should have a test.jpg now
\[11/07/2011 09:29:49\] SimonD: send link again
\[11/07/2011 08:29:15\] SimonD: Ok let me check, got the app installed, will run through thta with you.
\[11/07/2011 08:32:28\] SimonD: Ok got the test.jpg so that looks fine
\[11/07/2011 08:33:10\] Alexander Gee: Excellent. I'll endeavour to keep that up to date by hand for the next wee while and then switch in some logic at our end
\[11/07/2011 08:34:09\] SimonD: So I have the app installed and it is showing me two locations near me labelled KateWithPNGs
\[11/07/2011 08:34:28\] Alexander Gee: Both labeled that?
\[11/07/2011 08:34:42\] SimonD: yup
\[11/07/2011 08:35:10\] Alexander Gee: wait... how close are they? It is possible they are previous testing locations.
\[11/07/2011 08:37:34\] SimonD: Right next where it thinks my location is, will see if i can send a screen shot. I am indoors but  location is pretty close. I have WiFi only
\[11/07/2011 08:38:26\] Alexander Gee: Ok well that is good. I honestly have no idea aobut the user flow at the moment I've been server side for about a month, I need to look over the diagrams again.
\[11/07/2011 08:38:51\] Alexander Gee: I believe if you go to AR mode it sohuld load up the closest box for you
\[11/07/2011 08:43:44\] SimonD: not working, either over local wifi or from the hotel wifi.
\[11/07/2011 08:44:10\] SimonD: Any other checks I can do? I Sent you a screen dump from the ipad
\[11/07/2011 08:44:36\] Alexander Gee: Just got that thanks. I will ask, give me a sec
\[11/07/2011 08:47:10\] Alexander Gee: And what exactly happens when you click "View Box"?
\[11/07/2011 08:47:46\] SimonD: Just shows me a camera,
\[11/07/2011 08:47:57\] Alexander Gee: No loading spinner?
\[11/07/2011 08:48:13\] SimonD: No
\[11/07/2011 09:27:13\] Alexander Gee: <http://motim.dyndns.org/files/120.dat>
\[11/07/2011 09:29:59\] Alexander Gee: <http://motim.dyndns.org/files/120.dat>
\[11/07/2011 09:47:46\] Alexander Gee: Ok we are just doing a little test of this ourselves
\[11/07/2011 09:49:11\] Alexander Gee: Basically what I'm going to do is scale up the model and move it away from your location. We are thinking that since the model is inside your GPS inaccuracy it may be darting around in virtual space. (You have done a full 360 degree sweep to see if you can find it I assume)
\[11/07/2011 09:49:45\] SimonD: The guy with the iphone will be wit me in 1 hr, we are probably going to move to the Mother NY office to carry on testing.
\[11/07/2011 09:49:55\] Alexander Gee: Ok
\[11/07/2011 09:50:01\] SimonD: Yup is did 360 sphere ?
\[11/07/2011 09:50:15\] SimonD: Id id a up down and around
\[11/07/2011 09:50:21\] Alexander Gee: Cool (just checking everything off the list)
\[11/07/2011 09:51:05\] Alexander Gee: In the mean time cna you delete the app from the iPad and connect to the hotel wifi. Then reinstall the app and open it and go straight to "View Box" and check if you get a spinner
\[11/07/2011 09:51:22\] SimonD: OK
\[11/07/2011 09:51:31\] Alexander Gee: cheers
\[11/07/2011 09:55:00\] Alexander Gee: BTW I think our box is now acutally coming to us. Customs had stopped it because no one paid duty or got import clearance but we have done that and its on it way again.
\[11/07/2011 09:57:48\] SimonD: Cool, not sure how much its going to help.
\[11/07/2011 09:57:56\] SimonD: :-)
\[11/07/2011 10:04:38\] Alexander Gee: Do you have anything from that test?
\[11/07/2011 10:05:01\] SimonD: Still rsuncing the Ipad ,
\[11/07/2011 10:05:08\] SimonD: How about you?
\[11/07/2011 10:05:09\] Alexander Gee: Ok
\[11/07/2011 10:05:20\] SimonD: Working your end?
\[11/07/2011 10:05:57\] Alexander Gee: We confirmed that those settings make the model visible (not massive or one pixel across) and we tested at one of our barcelona placements on an iPhone 4
\[11/07/2011 10:06:25\] SimonD: Sorry which settings?
\[11/07/2011 10:06:57\] SimonD: Do i need to sdjust settings in the app?
\[11/07/2011 10:07:12\] Alexander Gee: Sorry no our scale position and height settings
\[11/07/2011 10:07:17\] Alexander Gee: server side
\[11/07/2011 10:07:24\] SimonD: Ok so defaults onthe app?
\[11/07/2011 10:07:38\] Alexander Gee: Yup they are pulled per model from the server.
\[11/07/2011 10:08:38\] SimonD: Ok should be ready to test in a bit I forgot to delete the video from the Ipad so it is backing up.
\[11/07/2011 11:15:26\] Alexander Gee: Having any luck?
\[11/07/2011 11:17:06\] SimonD: Yes, figure it out the default index.html got left in the build. I am just making a temporary one to test
\[11/07/2011 11:17:28\] Alexander Gee: ok
\[11/07/2011 11:17:49\] SimonD: How are you specifying the path currently?
\[11/07/2011 11:18:10\] Alexander Gee: hard coded string with the file names appended to the end of it
\[11/07/2011 11:19:22\] SimonD: <http://home/becksgreen/downloads/xxx.dat> ?
\[11/07/2011 11:19:59\] Alexander Gee: with the ip address yes
\[11/07/2011 11:20:22\] SimonD: ops yes
\[11/07/2011 11:21:19\] SimonD: so <http://192.168.201.73/home/becksgreen/downloads/xxx.dat> ?
\[11/07/2011 11:21:38\] Alexander Gee: that is it
\[11/07/2011 11:22:02\] SimonD: Ok will have it tested shortly
\[11/07/2011 11:23:00\] Alexander Gee: brilliant its hitting 3:30am  here
\[11/07/2011 11:44:20\] SimonD: Ok looks like its working
\[11/07/2011 11:44:30\] SimonD: I need to tidy it up a bit
\[11/07/2011 11:45:20\] SimonD: Will send you some stuff a bit later so you can replicate the key parts of the build to test locally.
\[11/07/2011 11:45:34\] Alexander Gee: Excellent
\[11/07/2011 11:46:55\] Alexander Gee: I'm going to hand you over to Mete now as I desperately need some sleep. His email is [mete.cakman@motim-technologies.com](mailto:mete.cakman@motim-technologies.com) he is up to date with what has been going on so far.
\[11/07/2011 11:47:42\] SimonD: Ok pass on my skype details
\[11/07/2011 11:47:48\] Alexander Gee: Will do
\[11/07/2011 11:47:53\] SimonD: THanks Alex :\_)
\[11/07/2011 11:48:06\] SimonD: Night
\[11/07/2011 11:48:14\] Alexander Gee: Have a good day

