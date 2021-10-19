# Dynamo2Relion
## A Tiny Function to Convert Dynamo Tables to Star Files for RELION 4.0

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/dynamo2m.svg)](https://pypi.python.org/pypi/dynamo2m/)

Based on [dynamo2m](https://github.com/alisterburt/dynamo2m) by Alister Burt.

## Installation

Installation is carried out via:
```sh
pip install dynamo2relion
```

## Requirements

Your directory containing the tilt series directories must be structured as follows:

```sh
TS_Directory #Directory containing all TS directories, link to this directory
|
--> TS_01 #Directory containing TS_01              
       |
       --> TS_01.mrc #TS_01  image stack. The file extension does not matter.        
|
--> TS_02              
       |
       -->TS_02.mrc  #
|
--> etc...
```

The program will ask you the path to TS_Directory. No directories other than the TS_* directories should be present in TS_Directory. Naming convention for the TS_* directories can be any mix of upper of lower case TS and any numbering convention desired. 

## Usage

Invoke from the command line via typing:
```sh
dynamo2relion
```
and input:
```sh
Input Dynamo table file: example.tbl
Output STAR file: test.star
Path to TS directory: /Path/to/directory/containing/all/ts/directories/as/shown/above
Binning level of Dynamo table (enter 1 for unbinned, binning is done using IMOD convention): 8
```

For binning level, simply enter 1 if the coordinates of your particles in the Dynamo table were picked from an unbinned tomogram. If the tomograms the particles were picked in were binned, add the correct binning level: binning is done using IMOD convention, i.e. for a pixel size of 1 A/px, a binning level of 8 would yield 8 A/px. 

Please note, as of v 0.0.3, the Euler angles are imported as rlnTomoSubtomogram<angles>. This will cause RELION to reconstruct subtomograms in the same orientation as the reference. If you do not want to do this, simply change the labels at the top of the star file to rlnAngle<angles>.
