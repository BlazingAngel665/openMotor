openMotor
==========

Overview
--------
openMotor is an open-source internal ballistics simulator for rocket motor experimenters. The software produces estimates of a rocket motor's chamber pressure and thrust based on input such as propellant properties and grain geometry. It uses the Fast Marching Method to determine how a propellant grain regresses, which allows the use of arbitrary core geometries. 

Current Features:
* Metric and imperial units
* Support for common grain geometries such as BATES, Finocyl, Star and more
* A propellant editor that allows the user to enter the properties of as many propellants as they wish
* The grain editor displays how a grain will regress to cut down on the guesswork involved in tweaking geometry
* ENG file exporting
* A UI that supports saving and loading designs along with undo and redo.

Planned Features:
* Erosivity simulation
* Loading custom grain geometry from SVG files
* Burnsim importing and exporting
* Detailed output of every calculated parameter at any time and position along the motor

The calculations involved were sourced from Rocket Propulsion Elements by George Sutton and from Richard Nakka's website (https://www.nakka-rocketry.net/rtheory.html).

Download
-------
The easiest way to use openMotor is to navigate to the 'releases' tab above and download latest version for your system. From there, just unzip the file and run it. 

Building from Source
--------------------
The program is currently being developed using python 3.6, but it also works with 3.7. The dependencies are outlined in `requirements.txt`, the main ones include `PyQt5`, `matplot`, `numpy`, `scipy`, `scikit-fmm`, and `scikit-image`. Because the PyQt5 bindings are used for the GUI, Qt5 must also be installed.

The easiest way to build/run from source code is to clone the repository and install the required dependencies into a virtual enviornment:
```
$ git clone https://github.com/reilleya/openMotor
$ cd openMotor
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

When everything is set up, you can start openMotor by running: `python main.py`
###### Note: On some systems, Python 2 and 3 are installed simultaneously, so you may have to specify which version to run when starting the venv. After the venv has been created, the programs `python` and `pip` are aliased to the python runtime specific for your venv, so use those (instead of `pip3` and `python3`, on e.g. Debian Linux)

#### UI Files:
openMotor uses Qt Designer to design the GUI, which generates `.ui` files describing the user interface. 
We use `pyuic5` to compile these files into Python source code which is then included in the program as ordinary source code.

To compile changes made to the `ui` files located in `uilib/views/forms`, use the command: `python setup.py build_ui`.  

License
-------
openMotor is released under the GNU GPL v3 license. The source code is distributed so you don't have to trust the calculations are being done correctly and can check for yourself if you doubt the results.

Contributing
------------
As openMotor is open source, one of the goals of the project is to have as many eyes on the code as possible. I believe this is the best way to avoid bugs and also the easiest way to get new features added to the software. If you have ideas on how to improve the program or find an error, please open an issue ticket for discussion or file a pull request if you would do it yourself.
