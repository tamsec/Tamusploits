How to detect and prevent ARP spoofing
======================================
This is obviously not a comprehensive review, but I'll just mention a few things that are relevant about how victims and network admins could detect this sort of thing

Victim: Detecting an attack
---------------------------
One of the first things a victim would notice, assuming SSLstrip works (which it often doesn't), is that sites that normally browse over HTTPS would be using HTTP instead. There will be no little green lock at the top of the URL and pages might be a little slower.


Admins: Detecting a host scan
-----------------------------
A precursor to this attack will almost always be a host scan, because the attacker has to know what IPs are active on the network in order to choose a victim. Luckily, due to the nature of a normal (non-newbie) scan, this is usally detectable by even the simplest self-made scripts. You could look for the following things:

* Any traffic between hosts on the same network except from router to other hosts (as opposed to hosts--> external network, which is normal traffic)
* Traffic from one host to more than a threshhold number of hosts (say, 5) within a certain time period
* An abnormal number of ARP requests within a certain time period. 

Setting time periods will be up to the discretion of the network admin. False positives are better than missed negatives!

Admins: Detecting an ARP spoof
------------------------------
This one involves probably a few more rules and obviously I don't know how real software does it, but you could look for the combination of these three things within a certain time period:

* Too many ARP responses from one host
* One host having too many IPs
* More than one host having a single IP

Admins: Just get someone else to do it all for you!
---------------------------------------------------
This is probably the best choice anyway--specialization rules. Let someone who has been doing this for years develop the software and use it. There are several IDS/IPS tools out there for free. However, the most respected and the one I'd recommend is Snort. 

Some important info about Snort
+++++++++++++++++++++++++++++++
There is literally so much to say about snort I'll just say go read the `docs <https://www.snort.org/documents>`_ if you're interested mostly. But there are a few key things to know. 

If you're a single user, no fear! Snort is free.

If you're using Snort in production for a business, the software itself is free but the meat of it--the actual rules it uses to detect and deter attacks, you'll have to pay. The rules aren't much, especially compared to software like Fireye. However, if you're rich enough, ever since Cisco bought Snort they also have a shiny multi-thousand dollar dashboard to go along with it. Most medium-sized businesses and larger will be willing to pay for their own IDS anyway most likely. 

If you're Target, you use FireEye and then ignore it when it warns you.