Tilde
==========

Tilde (or wwwtilda or ~) is a data organizer for computational materials science.

## Rationale

An efficient data management in computational materials science is a cornerstone, however still expensive and time-consuming. A nowadays scientific publication in this field is not a scholarship anymore, rather scholarship advertising. The actual scholarship is the software environment and the complete set of instructions which generate the figures for a publication. Here the situation with a plenty of incompatible data formats is very uncomfortable. Furthermore, a new approach to the data assessment and exchange is desired as the traditional peer-reviewed publications and their supplementary sections do not solve this task properly.

## Aims

Tilde aims to tackle these issues. Several popular computer simulation packages are currently supported: [VASP](http://www.vasp.at), [CRYSTAL](http://www.crystal.unito.it), [WIEN2K](http://www.wien2k.at), [GAUSSIAN](http://gaussian.com) and [EXCITING](http://exciting-code.org). The computational results can be automatically extracted into a repository, systemized and visualized. The example focus is on the vibrational and electronic properties of the crystalline materials: visualization of the band structures, densities of states, vibrational modes etc. Moreover, Tilde acts as an infrastructure for user's own scripts and self-written utilities, organizing them under single hood and assisting to pipe data throughout them. The third-party applications so could be integrated with Tilde using its application programming interface (**API**).

## Working principle

Tilde consists of several parts: core, local server, command-line interface (**CLI**) and graphical user interface (**GUI**). Core is responsible for data-mining and provides a number of APIs, which are employed by **CLI**, local server and **GUI**. User may manage core using **CLI** and/or **GUI**. Tilde local server is responsible for **GUI** and lives at the user own computer, acting as a small web-server. **GUI** is represented by a dynamic website, generated by server. This website displays a snapshot of user calculations and modeling results. All user data are private, they are stored securely on a local computer, protected by operating system and only available to current user.

## Prerequisites

Tilde core, local server and **CLI** are written in Python. On Windows no additional installations are required, as soon as all the dependencies (including Python interpreter itself) are already provided with Tilde. On Unix/Mac you should have Python (at least of version 2.6), as well as Numpy and sqlite3 Python modules pre-installed. Typically, this is the case: console command "python -c 'import numpy, sqlite3'" should produce no errors. Note, that Python 3 was not tested.

The graphical user interface (**GUI**) is written in JavaScript and runs in any modern HTML5 web-browser (e.g. Google Chrome, Mozilla Firefox or Safari). Flash and Java plugins are not required. For Windows, a suitable open-source web-browser Chromium is shipped with Tilde.

Tilde was tested on Windows XP, 7, 8 and Linux Debian and Suse operating systems.

## Usage

Please, avoid spaces and non-latin characters in the application folder name. The main script is called "tilde.bat" (for Windows) or "tilde.sh" (for Unix). All user commands are executed through this main script. To use command-line interface (**CLI**), run main script with a parameter (e.g. "-h" or "--help"). To start graphical interface (**GUI**), run main script without parameters. To terminate **GUI** on Windows, close the DOS box, on Unix hit Ctrl+C. On Unix **GUI** may also run in background mode ("nohup tilde.sh &"). Adding data is possible using both **CLI** and **GUI**. Avoid using **GUI** on large folders with data (more than several gigabytes), as **CLI** is much faster in this case.

## GUI hints

Hit key "q" to close all the popup windows. Use CTRL+mouse wheel to increase font size.

## Licensing

Tilde has [MIT-license](http://en.wikipedia.org/wiki/MIT_License). This means everybody is welcomed to use it for own needs for free or modify and adopt its source code.

## Download

Warning! This is **NOT** a public release, rather a proof-of-concept code summary for internal needs. It is not fully tested and may work unstable. However, the user data are sacred and will never be affected.

Use the right menu at [GitHub](http://github.com/jam31/wwwtilda) to download / clone in git.

## Related projects

Not only Tilde represents the community need for a new instrument in scientific data management and exchange. Other known related projects are:

- Accelrys Pipeline Pilot and Materials Studio, http://accelrys.com/products
- AFLOW framework and Aflowlib.org repository, http://www.aflowlib.org
- AIDA (AiiDA): Automated Infrastructure and Database for Ab-initio design (Bosch LLC), http://www.cecam.org/workshop-4-717.html?presentation_id=9102
- Blue Obelisk Data Repository (XSLT, XML), http://bodr.sourceforge.net
- CCLib (Python), http://cclib.sf.net
- CDF (Python), http://kitchingroup.cheme.cmu.edu/cdf
- CMR (Python), https://wiki.fysik.dtu.dk/cmr
- Computational Chemistry Comparison and Benchmark Database, http://cccbdb.nist.gov
- cctbx: Computational Crystallography Toolbox, http://cctbx.sourceforge.net
- ESTEST (Python, XQuery), http://estest.ucdavis.edu
- J-ICE online viewer (based on Jmol, Java), http://j-ice.sourceforge.net
- Materials Project (Python), http://www.materialsproject.org
- PAULING FILE world largest database for inorganic compounds, http://paulingfile.com
- pyCMW (Python), a framework of Max Planck Institute for Iron Research GmbH
- Quixote, http://quixote.wikispot.org
- Scipio (Java), https://scipio.iciq.es
- WebMO: Web-based interface to computational chemistry packages (Java, Perl), http://webmo.net

## Openness principle

The world wide web itself [was initiated](http://en.wikipedia.org/wiki/History_of_the_World_Wide_Web) as a mean of data exchange in the scientific community. The concept of a hyperlink came from scientific publications, being a way to reference the output of other scientists in the field. In this sense the principle of open data, open source scientific code and open standards is crucial. It is declared by an initiative group with a symbolic name [Blue Obelisk](http://www.jcheminf.com/content/3/1/37).

![Blue Obelisk logo and tagline](https://wwwtilda.googlecode.com/files/blue_obelisk.gif)

## Outlook

Tilde was inspired by torrents, Google Wave, Opera Unite and xmpp-jabber applications, whose common feature is a peer-to-peer (P2P) distributed syndication. Tilde will adopt this idea to materials science. That is, running instances of Tilde will be able to communicate with each other over the P2P-network, being located on the different computers. So Tilde users could connect and exchange their source / derivative data, compare their calculations and find out bugs together in modeling programs that they use for own data-mining.

## Contact

Please, send your feedback, bugreports and wishlists to [Evgeny Blokhin](mailto:eb@tilde.pro) or post them at [GitHub](http://github.com/jam31/wwwtilda/issues).

## Links

- http://github.com/jam31/wwwtilda
- http://twitter.com/wwwtilda
