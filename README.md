# Dynamo2Relion
## A Tiny Function to Convert Dynamo Tables to Star Files for RELION 4.0

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/dynamo2m.svg)](https://pypi.python.org/pypi/dynamo2m/)
[![PyPI version](https://badge.fury.io/py/dynamo2m.svg)](https://pypi.python.org/pypi/dynamo2m/)

Based on [dynamo2m][df1] by Alister Burt.

## Installation

Installation is carried out via:
```sh
pip install dynamo2relion
```

## Requirements

Your directory containing the tilt series directories must be structured as follows:

. TS_Directory #Directory containing all TS directories
\u251c\u2500\u2500 TS_01 #TS directory containing TS_01              
\u2502   \u251c\u2500\u2500 TS_01.mrc #TS_01  image stack. The file extension does not matter.        
\u251c\u2500\u2500 TS_02              
\u2502   \u251c\u2500\u2500 TS_02.mrc  #
\u2514\u2500\u2500 etc...

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
Path to TS directory: /Path/to/directory/containing/ts/directories/as/shown/above
```
