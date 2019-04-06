# Forensics Toolkit

This toolkit was prepared as part of IT 566 Digital Forenics class at BYU. It contains a digital database of tools and guides I use, write and discover during this course.


### [Acquisition](https://github.com/jharris1829/forensics-toolkit/#Acquisition)
### [Analysis](https://github.com/jharris1829/forensics-toolkit/#Analysis)
### [Other](https://github.com/jharris1829/forensics-toolkit/#Other)

## Acquisition

These tools are used in the acquisition of memory and disk images/data

### OSXPMEM

##### Description

A volatile memory acquisition tool that is part of the pmem suite of computer memory acquisition tools. It serves as a command-line utility for quickly and easily collecting RAM from a Macintosh system, formatting the output as an AFF4 volume.

##### My Thoughts

Osxpmem is an awesome command-line utility for quickly and easily collecting RAM from a Mac system. One of its greatest features is its output to an AFF4 volume, which has a ton of useful features. It was created by the same developers as Rekall and as such is very sound in terms of ability and reliability

##### Where to Find It

The software can be downloaded from the rekall github repository found [here](https://github.com/google/rekall/releases)


### DD

##### Description

dd is a command-line utility for Unix and Unix-like operating systems whose primary purpose is to convert and copy files. It has a simple, relatively intuitive syntax and a useful set of options to extend its basic capabilities. A good guide to using this tool can be found [here](http://www.forensicfocus.com/linux-dd-basics)

##### My Thoughts

I loved using dd. Like many Unix tools, it was very intuitive and worked as expected. We paired it with netcat to send a disk image to a forensics computer and it was very quick and easy.

##### Where to Find It

On almost any Unix distro! See the guide linked about for help with usage.


### LiME

##### Description

LiME (formerly DMD) is a Loadable Kernel Module (LKM), which allows the acquisition of volatile memory from Linux and Linux-based devices, such as those powered by Android. The tool supports acquiring memory either to the file system of the device or over the network.

##### My Thoughts

LiME took us a minute to get used to (although I think that was partially due to my inxeperience with Linux modules). All in all though I was very impressed with the speed, and the ability to transfer the memory dump across a network was very helpful in getting the memory to a machine where it could be analyzed.

##### Where to Find It

[Downloads and usage guide](https://github.com/504ensicsLabs/LiME)

* LiME does needs to be built from source which will vary by Unix distro so keep that in mind as you are using it

### Netcat

##### Description

netcat (often abbreviated to nc) is a computer networking utility for reading from and writing to network connections using TCP or UDP. The command is designed to be a dependable back-end that can be used directly or easily driven by other programs and scripts. At the same time, it is a feature-rich network debugging and investigation tool, since it can produce almost any kind of connection its user could need and has a number of built-in capabilities.

##### My Thoughts

Netcat is a must have for any forensic investigator and really for anyone in the technology industry. It has so many features that can help with anything from diagnosing network issues to transferring files to performing penetration tests. The source code has been around long enough that the code is reliable and there are plenty of great usage guides.

##### Where to Find It

One of the best ways to get netcat is as part of the Nmap package download found [here](https://nmap.org/ncat/)

### FTK Imager

##### Description

FTK Imager is a full service forensic application developed by AccessData that is in wide use by government and law enforcement. With many of the same features as EnCase, this may be an alternative that digital forensic analysts will want to explore. The FTK Imager is a simple but concise tool. It saves an image of a hard disk in one file or in segments that may be later on reconstructed. It calculates MD5 hash values and confirms the integrity of the data before closing the files.

##### My Thoughts

FTK Imagers is widely considered as one of the best in the business in forensic acquisition and after using it myself I can see why. It was quick and easy to use, it had options to save case numbers, and other important details relevant to the acquisition and worked flawlessly.

##### Where to Find It

AccessData has made FTK Imager a free download which you can get [here](https://accessdata.com/product-download/ftk-imager-version-4.2.1)


## Analysis

These tools are used for forensic analysis of memory dumps, disk images, and other data.

### Autopsy

##### Description

Autopsy® is a digital forensics platform and graphical interface to The Sleuth Kit® and other digital forensics tools. Autopsy was designed to be an end-to-end platform with modules that come with it out of the box and others that are available from third-parties. Some of the modules provide:
* Timeline Analysis - Advanced graphical event viewing interface (video tutorial included).
* Hash Filtering - Flag known bad files and ignore known good.
* Keyword Search - Indexed keyword search to find files that mention relevant terms.
* Web Artifacts - Extract history, bookmarks, and cookies from Firefox, Chrome, and IE.
* Data Carving - Recover deleted files from unallocated space using PhotoRec
* Multimedia - Extract EXIF from pictures and watch videos.
* Indicators of Compromise - Scan a computer using STIX.


##### My Thoughts

I really enjoyed Autopsy although felt overwhemed at some points due to just how much information it provided, I'm sure as I gain more exprience it will be a tool I will love having in my toolkit.

##### Where to Find It

Autopsy can be found as part of the sleuth kit [here](https://www.sleuthkit.org/autopsy/)

Being an open source project there are some good videos about [installation](https://www.youtube.com/watch?v=PvHgR1poU5s), [extensive demos](https://www.youtube.com/watch?v=Smy4mj293GE), and [in-depth feature tutorials](https://www.youtube.com/watch?v=FJqoUakfmdo&t=148s)


### Rekall

##### Description

The Rekall Framework is a completely open collection of tools, developed by Google, implemented in Python under the Apache and GNU General Public License, for the extraction and analysis of digital artifacts computer systems.

##### My Thoughts

Rekall ended up being more difficult to install on my system than I thought it would be (my own fault for using Windows...), but after it was installed it was a very in depth tool. It uses modules to parse through the memory and output information but some modules only work for certain operating systems and the outputs can be hard to read. It's not a simple plug and play tool but with experience it could be very valuable

##### Where to Find It

Rekall is available as a python package installable via the pip package manager. To install it, first create a virtal env, switch to it and then install rekall:
```
$ virtualenv  /tmp/MyEnv
 New python executable in /tmp/MyEnv/bin/python
 Installing setuptools, pip...done.
 $ source /tmp/MyEnv/bin/activate
 $ pip install --upgrade setuptools pip wheel
 $ pip install rekall-agent rekall
```
For windows, Rekall is also available as a self contained installer package. Please check the download page for the most appropriate installer to use [Rekall-Forensic.com](http://www.rekall-forensic.com/)


### Snort

##### Description

A free, open source network intrusion detection and prevention system capable of performing real-time traffic analysis and packet logging on IP networks. Initially called a “lightweight” intrusion detection technology, Snort has evolved into a mature, feature-rich IPS technology that has become the de facto standard in intrusion detection and prevention. With over 4 million downloads and nearly 400,000 registered users, it is the most widely deployed intrusion prevention technology in the world.

##### My Thoughts

Snort can be very helpful in finding the needle of an issue in a haystack of logs and network traffic. Snort was very helpful in finding where to further investigate. However an IDS system is only as good as its definitions and rules. With ample time given to setting up proper rules for an environment, Snort could be a very good resource.

##### Where to Find It

Installation for both Unix and Windows OS can be found [here](https://www.snort.org/)


### Volatility

##### Description

The Volatility Framework is an open source collection of tools, implemented in Python under the GNU General Public License, for the extraction of digital artifacts from volatile memory (RAM) samples. The extraction techniques are performed completely independent of the system being investigated but offer visibility into the runtime state of the system. The framework is intended to introduce people to the techniques and complexities associated with extracting digital artifacts from volatile memory samples and provide a platform for further work into this exciting area of research.

##### My Thoughts

While Volatility provides many of the same features Rekall does (both Python based, both command-line based, both intended for memory analysis) Volatility requires the use of profiles, which are difficult to both obtain and use, especially if the computer you are working with is not a common OS release or is too new for a proper profile to have been built. Additionally, Volatility seems to be much slower than Rekall in performing standard memory analysis procedures.

##### Where to Find It

The Volatility tool is available for Windows, Linux and Mac operating system ([source](https://github.com/volatilityfoundation/volatility/wiki/Installation)). For Windows and Mac OSes, [standalone executables](https://www.volatilityfoundation.org/releases) are available and it can be installed on Ubuntu 16.04 LTS using following command.

```apt-get install volatility```

Usage notes:
>The Volatility tool is used to determine that either the PC is infected or not. As we know that, the malicious program can be extracted from the running processes from the memory dump.  So, first of all, it is required to identify the supported “profiles” for the dumped memory image. The ```imageinfo``` command is used to identify the “profiles” for the image.


### Wireshark

##### Description

Wireshark is a network packet analyzer. A network packet analyzer will try to capture network packets and tries to display that packet data as detailed as possible.

You could think of a network packet analyzer as a measuring device used to examine what’s going on inside a network cable, just like a voltmeter is used by an electrician to examine what’s going on inside an electric cable (but at a higher level, of course).

In the past, such tools were either very expensive, proprietary, or both. However, with the advent of Wireshark, all that has changed.

##### My Thoughts

Wireshark is hands down the best network and packet analyzer. Part of it's strength lies in the filters that you are able to place and then the ability to track the transmission stream to find out exactly what happened. Network traffic is so vital in digital forensics and Wireshark will be at the forefront of those investigations

##### Where to Find It

[System Requirement](https://www.wireshark.org/docs/wsug_html_chunked/ChIntroPlatforms.html)

[Downloads](https://www.wireshark.org/download.html)


### WinPrefetchView

##### Description

WinPrefetchView is a small utility that reads the Prefetch files stored in your system and displays the information stored in them. By looking in these files, you can learn which files every application is using, and which files are loaded on Windows boot.

WinPrefetchView Key Features:
* View files that are prefetched when applications are loaded up
* See the file relationships between applications and other files they access
* Examine files that Windows uses when booting up
* Possible to use as a diagnostic tool with files infected with a virus

##### My Thoughts

Prefetch files are very valuable in forensic investigations when it comes to determine a timeline of events and files. Autopsy also has the ability to see prefetch files but WinPrefetchView is specifically target to these files and as such does a very good job of analyzing them.

##### Where to Find It

WinPrefetchView can be found at [NirSoft](https://www.nirsoft.net/utils/win_prefetch_view.html)


### VirusTotal

##### Description

A free service that analyzes files and URLs for viruses, worms, trojans and other kinds of malicious content. Fortune 500 companies, governments and leading security companies are all part of the VirusTotal community, which has grown to over 500,000 registered users.

##### My Thoughts

VirusTotal aggregates many antivirus products and online scan engines to check for viruses that the user’s own antivirus may have missed, or to verify against any false positives. It is a very useful site if you are able to get a hold of a potentially dangerous file without a way to sandbox or safely work with it yourself.

##### Where to Find It

[VirusTotal](https://www.virustotal.com/#/home/upload)


### Ghidra

##### Description

Ghidra is a software reverse engineering (SRE) framework created and maintained by the National Security Agency Research Directorate. This framework includes a suite of full-featured, high-end software analysis tools that enable users to analyze compiled code on a variety of platforms including Windows, macOS, and Linux. Capabilities include disassembly, assembly, decompilation, graphing, and scripting, along with hundreds of other features. Ghidra supports a wide variety of processor instruction sets and executable formats and can be run in both user-interactive and automated modes. Users may also develop their own Ghidra plug-in components and/or scripts using Java or Python.

##### My Thoughts

I have yet to use Ghidra but the NSA has an incredible cyber security division and has some of the most powerful tools in the industry. Some top security engineers and analysts have stated that Ghidra is more powerful and usable than any other SRE tool on the market.

##### Where to Find It

Ghidra can be downloaded from the NSA's GitHub repository [here](https://github.com/NationalSecurityAgency/ghidra)


## Other

These tools were written by me for specific application or use but the code can be altered for other applications

### hashFiles

##### Description

This tool was written in python and can be used to obtain hashes for all the files in a given directory. It utilizes the hashlib python library

##### Source Code

Found in this repository under the name hashFiles.py and found below:

```
import os, os.path
import sys
import hashlib

cwd = os.getcwd()

for file in os.listdir(cwd):
    filename = os.fsdecode(file)
    if filename != 'hashFiles.py' and not filename.startswith('Hash_'):
        BLOCKSIZE = 65536
        md_hasher = hashlib.md5()
        with open(file, 'rb') as afile:
            print('Hashing MD5 for: ' + filename)
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                md_hasher.update(buf)
                buf = afile.read(BLOCKSIZE)

        BLOCKSIZE = 65536
        sha_hasher = hashlib.sha1()
        with open(file, 'rb') as afile:
            print('Hashing SHA1 for: ' + filename)
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                sha_hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        
        print('Writing Hash File')
        hash_file_name = 'Hash_' + filename + '.txt'
        with open(hash_file_name, "w") as hfile:
            hfile.write("MD5: " + md_hasher.hexdigest() + "\n")
            hfile.write("SHA1: " + sha_hasher.hexdigest())
        hfile.close()
```


### scrapeData

##### Description

This tool was written in python for scraping data from a sports website. The code was customized for a specific purpose, however it can easliy be altered to grab data for any use. It utilizes the BeautifulSoup library.

##### Source Code

Found in this repository under the name scrapeData.py
