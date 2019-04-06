# forensics-toolkit

This toolkit was prepared as part of IT 566 Digital Forenics class at BYU. It contains a digital database of tools and guides I use, write and discover during this course.

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


### Rekall

##### Description

##### My Thoughts

##### Where to Find It


### Rekall

##### Description

##### My Thoughts

##### Where to Find It


### Rekall

##### Description

##### My Thoughts

##### Where to Find It


### Rekall

##### Description

##### My Thoughts

##### Where to Find It


### Rekall

##### Description

##### My Thoughts

##### Where to Find It









```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
